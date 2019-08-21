from django.urls import path, include
from . import views
from django.contrib import admin

# admin.site.site_header = 'Flight Booking Admin'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('authorize/',  views.index, name='authorize'),
    path('verify/', views.verify, name='verify'),
    path('email/', views.send_email, name='email'),
    path('', views.pic, name='get_pic')
]