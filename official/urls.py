from . import views
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
    path('delete_comment/<slug:slug>/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),# urls for deleting comment
    path('official_news/<slug:slug>/', views.official_news, name='official_news'),
    path('<slug:slug>/edit_comment/<int:comment_id>', # The comment form's action attribute points to the URL for the comment_edit view, with the ID of the selected comment
         views.comment_edit, name='comment_edit'), # urls for editing comment
    path('like_comment/', views.like_comment, name='like_comment'),
]