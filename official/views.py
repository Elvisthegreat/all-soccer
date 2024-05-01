from django.shortcuts import render, get_object_or_404
from django.views import generic
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

