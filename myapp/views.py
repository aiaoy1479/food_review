from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cate(request):
    return render(request, 'cate.html')

def review(request):
    return render(request, 'reviews.html')

def search(request):
    return render(request, 'search.html')
