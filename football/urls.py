from . import views
from django.urls import path


urlpatterns = [
    path('', views.FootballList.as_view(), name="home"),
    path('preview1/<slug:slug>/', views.preview1, name='preview1'),
    path('preview2/<slug:slug>/', views.preview2, name='preview2'),
    path('preview3/<slug:slug>/', views.preview3, name='preview3'),

]