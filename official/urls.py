from . import views
from django.urls import path


urlpatterns = [
    path('official/', views.OfficialList.as_view(), name='official'),
    path('official_news/<slug:slug>/', views.official_news, name='official_news'),
]