from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse     # import http
from .models import Item    # import  class , i mean db
from .forms import ItemForm

# from django.views.generic.list import ListView

def index(request):
    # return HttpResponse("hello")
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)


# class IndexClassView(ListView):
#     model=Item
#     template_name='food/index.html'
#     context_object_name='item_list'

    
    
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
        item = form.save(commit=False)
        print(item)
            # Set the user_name field to the currently logged-in user.
        item.user_name = request.user
            
            # Now, save the item with the user_name field set.
        item.save()
        print(item)
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