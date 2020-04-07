import datetime
from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# Create your views here.
from product.models import Products

def temp(request):
    return render(request , 'product/product.html')

def shop(request):
    all_products = Products.objects.filter(available=True).order_by('-ranking' , '-created_at')

    if  all_products:

        print("Displaying Products!")
        num_products = all_products.count()
        if num_products > 12:
            pages = num_products/12
            orphans = num_products % pages
        else:
            pages = 1
            orphans = 0

        paginator = Paginator(all_products, 12 , orphans) # Show 12 products per page
        page = request.GET.get('page')
        products = paginator.get_page(page)
        ttl_page = int(pages)
        list = []
        for i in range(1, ttl_page+1):
            list.append(i)

        now = datetime.date.today()
        few_weeks = now - datetime.timedelta(days=14)

        context = { 'products' : products , 'list' : list , 'few_weeks' : few_weeks}
        return render(request , 'product/product.html', context)
    else:
        return render(request , 'product/product.html')


def product_info(request, product_slug):

    #return HttpResponse("<h2> say hello! : "+ str(article_id) +" and category is :" + str(category_id) +  "</h2>")
    try:

        product_info = Products.objects.get(slug = product_slug)

        print("===================================")
        print("===================================")
        print("===================================")

        all_products = Products.objects.filter(available=True).order_by('-ranking' , '-created_at')

        context = { 'product_info' : product_info , 'related_products' : all_products}
        

        return render(request , 'product/product-info.html' , context)


        # now = datetime.date.today()
        # few_weeks = now - datetime.timedelta(days=14)
        # P_ranking = product_info.ranking
        # P_type = product_info.product_type
        # try:
        #     products_by_type = Products.objects.filter(available=True , product_type=P_type).\
        #         exclude(title=product_info.title).order_by('-ranking' , '-created_at')
        #     products_by_rank =  Products.objects.filter(available=True , ranking=P_ranking).\
        #         exclude(title=product_info.title).order_by('-ranking' , '-created_at')
        #     related_products = (products_by_type | products_by_rank).distinct()
        #     context = { 'product_info' : product_info  , 'few_weeks' : few_weeks , 'related_products' : related_products}
        #     return render(request , 'product/product-detail.html' , context)
        # except:
        #     context = {'product_info' : product_info }
        #     return render(request , 'product/product-detail.html' , context)
    except:
        return render(request , 'error.html')

