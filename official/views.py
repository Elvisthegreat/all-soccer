from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Official, Comment

# Create your views here.


class OfficialList(generic.ListView):
    queryset = Official.objects.all().order_by("-created_on")
    template_name = "official/official.html"
    paginate_by = None



def official_news(request, slug):
    queryset = Official.objects.all()
    officials = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "official/official_news.html",

        {
            'officials': officials,
        },
    )

