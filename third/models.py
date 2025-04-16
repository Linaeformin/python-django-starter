from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=200)

    password = models.CharField(max_length=20, default=None, null=True)    #기존에 입력된 데이터들은 패스워드를 걸지 않음
    image = models.CharField(max_length=500, default=None, null=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Review(models.Model):
    point=models.IntegerField()
    comment=models.CharField(max_length=500)

    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)    #많은 것(many)에 해당되는 곳에 작성

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
