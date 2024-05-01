from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Official, Comment
from .forms import CommentForm

# Create your views here.


class OfficialList(generic.ListView):
    queryset = Official.objects.all().order_by("-created_on")
    template_name = "official/official.html"
    paginate_by = None



def official_news(request, slug):
    queryset = Official.objects.all()
    officials = get_object_or_404(queryset, slug=slug)
    comments = officials.comments.all().order_by("created_on")
    comment_count = officials.comments.all().count()

    """Handling the Post request from the comment form"""
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.officials = officials
            comment.save()
            # for successfully message
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted successfully'
            )

    comment_form = CommentForm()
    
    return render(
        request,
        "official/official_news.html",

        {
            'officials': officials,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":

        queryset = Official.objects.all()
        officials = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user: # checking aain if the form is valid and if it still same user
            comment = comment_form.save(commit=False)
            comment.officials = officials
            comment.approved = False # Turn the previous approved commemt to unapproved
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('official_news', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Official.objects.all()
    officials = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('official_news', args=[slug]))


