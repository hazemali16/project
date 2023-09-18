from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf import settings

from . import views


urlpatterns = [
    path('', views.Home, name="home"),
    path('profile', views.profile, name="profile"),
    path('post', views.post),
    # path('api/', views.api),
    path('user-profile/<int:postId>/', views.user_profile, name="user_profile"),
    path('edit/<int:postId>', views.edit),
    path('delete/<int:postId>', views.delete),
    
]
