from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('viewblog/',views.viewblog,name='viewblog'),
    path('createblog/',views.createblog,name='createblog'),
    path('search/',views.search,name='search')
]