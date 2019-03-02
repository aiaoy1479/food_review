from django.shortcuts import render
from .models import Review, Cate, Menu, Shop

def index(request):
    last_review = Review.objects.all().last()[0:6]
    return render(request, 'index.html', {'last_review': last_review})

def cate(request):
    return render(request, 'cate.html')

def review(request,shop_id):
    shops = Shop.objects.get(id=shop_id)
    last_review = Review.objects.filter(pk=shop_id).last()
    #if last_review is not None:
    #    last_review = last_review[0:3]
    if request.POST:
        rate = request.POST['rating']
        body_new = request.POST['discuss']
        wri_name = request.POST['name']
        new_review = Shop.objects.get(id=shop_id)
        new_review.review_set.create(rating=rate, writer_name=wri_name, body=body_new)
        
    return render(request, 'reviews.html',{'shop': shops, 'shop_id':shop_id, 'last_review': last_review})

def search(request):
    shops = ""
    if request.GET:
        shops = Shop.objects.filter(name__contains=request.GET['q'])
    return render(request, 'search.html', {'shop': shops})
    
    
