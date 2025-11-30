from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('make-scrape', views.make_scrape, name='make_scrape'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('logout', views.LogOut, name='logout'),

]

