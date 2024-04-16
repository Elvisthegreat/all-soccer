from . import views
from django.urls import path


urlpatterns = [
    path('', views.OfficialList.as_view(), name='official'),
    path('<slug:slug>/', views.official_news, name='official_news'),
]