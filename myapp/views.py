from django.shortcuts import render
from .models import Shop, Review, Menu

def index(request):
    last_review = Review.objects.order_by('-id')[0:6]
    return render(request, 'index.html', {'last_review': last_review})

def cate(request):
    return render(request, 'cate.html')

def review(request,shopID):
    shops = Shop.objects.get(id=shopID)
    recent_review = Review.objects.filter(shop_id=shopID).order_by('-id')
    if recent_review:
        recent_review = recent_review[0:3]
    if request.POST:
        rate = request.POST['rating']
        body_new = request.POST['discuss']
        wri_name = request.POST['name']
        new_review = Shop.objects.get(id=shopID)
        new_review.review_set.create(rating=rate, writer_name=wri_name, body=body_new)
        
    return render(request, 'reviews.html',{'shop': shops, 'recent_review': recent_review})

def search(request):
    shops = ""
    if request.GET:
        shops = Shop.objects.filter(name__contains=request.GET['q'])
    return render(request, 'search.html', {'shop': shops})
    
    
