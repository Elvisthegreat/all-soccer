from . import views
from django.urls import path


urlpatterns = [
    path('', views.FootballList.as_view(), name="home"),
    path('preview1/<slug:slug>/', views.preview1, name='preview1'),
    path('preview2/<slug:slug>/', views.preview2, name='preview2'),
    path('preview3/<slug:slug>/', views.preview3, name='preview3'),
    path('preview4/<slug:slug>/', views.preview4, name='preview4'),
    path('preview5/<slug:slug>/', views.preview5, name='preview5'),
    path('preview6/<slug:slug>/', views.preview6, name='preview6'),

    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),

]