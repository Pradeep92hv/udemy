from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse     # import http
from .models import Item    # import  class , i means= db
from .forms import ItemForm

def index(request):
    # return HttpResponse("hello")
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)


def detail(request,id):
    # return HttpResponse("id i: %s " %item_id )
    item=Item.objects.get(id=id)
    context={
        'item':item,
    }
    
    return render(request,'food/details.html',context)



def create_item(request):
    form=ItemForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')  #namespacing
    
    return render(request,'food/item-form.html',{'form':form})


def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/delete-item.html',{'item':item})