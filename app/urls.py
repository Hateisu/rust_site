from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('rustvideo/<int:id>', views.rustvideobyid, name='rustvideo'),
    path('dotavideo/<int:id>', views.dotavideobyid, name='dotavideo'),
]