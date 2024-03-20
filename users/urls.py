from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update-profile'),
	path('login', views.applogin, name='login'),
    path('logout', views.applogout, name='logout'),
]