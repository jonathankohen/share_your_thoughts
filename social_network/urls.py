from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('home', views.home),
    path('login', views.login),
    path('logout', views.logout),
    path('add_post', views.add_post),
    path('create_post', views.create_post),
    path('like/<int:post_id>', views.like_post),
    path('unlike/<int:post_id>', views.unlike),
    path('delete/<int:post_id>', views.delete),
    path('posts/<int:post_id>', views.show),
]