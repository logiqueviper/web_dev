from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('option/',views.option,name='blog-option'),
    path('register_here/',views.getdata,name = 'blog-getdata'),
    path('display_data/',views.display_rel_data,name = 'blog-display_data'),
    path('inp_data/',views.inp_data,name='bolg-get_detail'),
]
