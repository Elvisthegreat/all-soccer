from . import views
from django.urls import path


urlpatterns = [
    path('official/', views.OfficialList.as_view(), name='official'),
    path('official_news/<slug:slug>/', views.official_news, name='official_news'),
    path('<slug:slug>/edit_comment/<int:comment_id>', # The comment form's action attribute points to the URL for the comment_edit view, with the ID of the selected comment
         views.comment_edit, name='comment_edit'), # urls for editing comment
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),# urls for deleting comment
]