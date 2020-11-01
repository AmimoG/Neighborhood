from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search_project, name='search'),
]
