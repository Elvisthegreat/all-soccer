from . import views
from .views import like_official
from django.urls import path


"""
Remember the "edit_comment" and "delete _comment" in the urlpattern are not found in our
template neither in our model or our workspace, this are dynamically updated to the URL for
the comment_edit view function and comment_delete view function
"""
"""
path for our url
""" 

urlpatterns = [
    path('official/', views.OfficialList.as_view(), name='official'),
    path('official_news/<slug:slug>/', views.official_news, name='official_news'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'), # urls for editing comment
    path('delete_comment/<slug:slug>/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),# urls for deleting comment,
    path('official/like/<slug:slug>/', views.like_official, name='like_official'),
]