from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

import random

def index(request): #유저가 요청하면
    now=datetime.now()
    context={
        'current_date':now
    }  #삽입하거나 치환할 변수 삽입, key-value로 매핑
    return render(request, 'first/index.html', context)

def select(request):
    context={}
    return render(request, 'first/select.html', context)


def result(request):
    chosen=int(request.GET['number'])

    results=[]
    if 1 <= chosen <= 45:
        results.append(chosen)

    box=[]
    for i in range(0,45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) <6:
        results.append(box.pop())

    context={
        'numbers':results
    }
    return render(request, 'first/result.html', context)
