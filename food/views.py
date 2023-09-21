from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse     # import http
from .models import Item    # import  class , i means= db


def index(request):
    # return HttpResponse("hello")
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)


def detail(request,item_id):
    # return HttpResponse("id i: %s " %item_id )
    item=Item.objects.get(id=item_id)
    context={
        'item':item,
    }
    
    return render(request,'food/details.html',context)