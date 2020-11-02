from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload, name='upload'),
    path('account/', include('django.contrib.auth.urls')),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/', views.profile, name='profile'),
    path('profile/<username>/', views.edit_profile, name='edit_profile'),
]
