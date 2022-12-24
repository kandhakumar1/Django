
from django.shortcuts import render,redirect
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages

def home(request):
    products=product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})

def register(request):
    form=CustomUserForm()
    return render(request,"shop/register.html",{"form":form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"Catagory":catagory})

def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=product.objects.filter(Catagory__name=name)
        return render(request,"shop/products/index.html",{"products":products,"Catagory_name":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')


def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(product.objects.filter(name=pname,status=0)):
             products=product.objects.filter(name=pname,status=0).first()
             return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Catagory Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('collections')