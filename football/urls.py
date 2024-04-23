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
    path('psg_history/<slug:slug>/', views.psg_history, name='psg_history'),
    path('real_madrid_history/<slug:slug>/', views.real_madrid_history, name='real_madrid_history'),
    path('man_City_history/<slug:slug>/', views.man_city_history, name='man_city_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
    path('barcelona_history/<slug:slug>/', views.barcelona_history, name='barcelona_history'),
]