from django.shortcuts import render
from .models import Review, Cate, Menu, Shop

def index(request):
    last_review = Review.objects.all().last()[0:6]
    return render(request, 'index.html', {'last_review': last_review})

def cate(request):
    return render(request, 'cate.html')

def review(request,shop_name):
    shops = Shop.objects.get(id=shop_name)
    last_review = Review.objects.filter(id=shop_name).last()
    if last_review:
        last_review = last_review[0:3]
    if request.POST:
        title = shop_name
        rating = request.POST['rating']
        body = request.POST['discuss']
        wriname = request.POST['name']
        review = Review(titles=title, ratings=rating, writer_names=wriname, bodys=body)
        review.save()
    return render(request, 'reviews.html',{'shop': shops, 'shop_name':shop_name, 'last_review': last_review})

def search(request):
    shops = ""
    if request.GET:
        shops = Shop.objects.filter(name__contains=request.GET['q'])
    return render(request, 'search.html', {'shop': shops})
    
    
