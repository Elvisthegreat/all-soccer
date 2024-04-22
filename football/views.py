from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Football

# Create your views here.


class FootballList(generic.ListView):
    queryset = Football.objects.all().order_by("-created_on")
    template_name = "football/index.html"
    paginate_by = 6


def preview1(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "football/preview1.html",

        {
            'ball': ball,
        },
    )


def preview2(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)

    return render(
        request, 'football/preview2.html',

        {
            'ball': ball,
        },
    )

def preview3(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)

    return render(
        request, 'football/preview3.html',
        {
            'ball': ball,
        },
    )

def preview4(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)

    return render(
        request, 'football/preview4.html',
        {
            'ball': ball,
        },
    )

def preview5(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)

    return render(
        request, 'football/preview5.html',
        {
            'ball': ball,
        },
    )

def preview6(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)

    return render(
        request, 'football/preview6.html',
        {
            'ball': ball,
        },
    )

    # Club history section

def barcelona_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/barcelona_history.html',
        {
            'ball': ball,
        },
    )