from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
