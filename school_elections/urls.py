from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('results/', views.results_view, name='results'),
    path('vote', views.vote_view, name='vote'),
]
