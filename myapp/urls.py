from django.urls import path
from . import views

urlpatterns = [
        path('index/', views.index, name='index'),
        path('<int:shopID>/', views.review, name='review'),
        path('categories/', views.cate, name='cate'),
        path('search/', views.search, name='search'),
]
