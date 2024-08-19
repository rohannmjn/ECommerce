from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Q

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products': latest_products
    }
    return render(request,"index.html",context)

def list_products(request):
    
    
    page=1
    if request.method=="GET":
        page = request.GET.get('page',1)
        product_list=Product.objects.order_by('-priority')
        product_paginator=Paginator(product_list,2)
        product_list=product_paginator.get_page(page)
        context={'products':product_list}
        return render(request,"products.html",context)
    else:
        query = request.POST.get('q', '')
        
        if query:
            results = Product.objects.filter(title__icontains=query, delete_status=Product.LIVE)
        print(results)
        context={'products':results}
        return render(request,"products.html",context)
           


def detail_products(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    
    return render(request,"products_details.html",context)



