from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Football

# Create your views here.


class FootballList(generic.ListView):
    queryset = Football.objects.all().order_by("-created_on")
    template_name = "football/index.html"
    paginate_by = 6


def football_preview(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "football/football_preview.html",

        {
            'ball': ball,
        },
    )

