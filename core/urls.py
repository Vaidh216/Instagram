from django.urls import path
from . import views

from django.views.static import serve
from django.conf.urls import re_path
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('logout',views.logout, name='logout'),
    path('settings',views.settings, name='settings'),
    path('upload',views.upload, name='upload'),
    path('like-post',views.like_post, name='like-post'),
    path('profile/<str:pk>',views.profile, name='like-profile'),
    path('follow',views.follow, name='follow'),
    path('search',views.search, name='search'),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]