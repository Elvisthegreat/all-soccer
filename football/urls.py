from . import views
from django.urls import path


urlpatterns = [
    path('', views.FootballList.as_view(), name="home"),
    path('<slug:slug>/', views.football_history, name='football_history'),
]