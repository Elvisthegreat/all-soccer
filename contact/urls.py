from . import views
from django.urls import path

"""check the name of your function then add for 
contact_us, use it for the views."""

urlpatterns = [
    path('', views.contact, name='contact'),
]