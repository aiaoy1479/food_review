from django.shortcuts import render

def index(request):
    render(request, 'index.html')

def cate(request):
    render(request, 'cate.html')

def review(request):
    render(request, 'reviews.html')

def search(request):
    render(request, 'search.html')
