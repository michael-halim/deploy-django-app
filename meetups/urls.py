from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index_page'),
    path('<slug:slug>/success',views.confirm_registration,name='success-page'),
    path('<slug:slug>',views.meetups_details,name='detail-page'),
]
