from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls import url

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

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]