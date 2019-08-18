from django.urls import path, include
from . import views
from django.contrib import admin

# admin.site.site_header = 'Flight Booking Admin'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('pic/', views.pic, name='get_pic'),
    path('run_sh/',  views.index, name='run_sh'),
    path('verify/', views.verify, name='verify')
]