from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.login, name='Login'),
    path('home', views.home, name='Home'),
    path('Queries/', views.Queries, name='Queries'),
    path('index/', views.Index.as_view(), name='index'),
    path('Details/', views.info, name='Details'),
    re_path(r'^chat/(?P<room_name>\w+)/$', views.Room.as_view(), name='room'),
    path('logout/', views.logout, name='logout'),
    ] #<str:room_name>
