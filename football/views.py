from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Football
from .forms import CommentForm

# Create your views here.


class FootballList(generic.ListView):
    queryset = Football.objects.all().order_by("-created_on")
    template_name = "football/index.html"
    paginate_by = 6


def preview1(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    comments = ball.comments.all().order_by("-created_on")



    return render(
        request,
        "football/preview1.html",

        {
            'ball': ball,
            "comments": comments,
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

def psg_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/psg_history.html',
        {
           'ball': ball,
        },
   )

def real_madrid_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/real_madrid_history.html',
        {
           'ball': ball,
        },
   )

def man_city_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/man_city_history.html',
        {
           'ball': ball,
        },
   )
def newcastle_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/newcastle_history.html',
        {
           'ball': ball,
        },
   )

def chelsea_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/chelsea_history.html',
        {
           'ball': ball,
        },
   )

def bayern_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/bayern_history.html',
        {
           'ball': ball,
        },
   )

def arsenal_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/arsenal_history.html',
        {
           'ball': ball,
        },
   )

def bvb_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/bvb_history.html',
        {
           'ball': ball,
        },
   )

def inter_milan_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/inter_milan_history.html',
        {
           'ball': ball,
        },
   )

def lpool_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/lpool_history.html',
        {
           'ball': ball,
        },
   )

def porto_history(request, slug):
    queryset = Football.objects.all()
    ball = get_object_or_404(queryset, slug=slug)
    return render(
        request, 'football/porto_history.html',
        {
           'ball': ball,
        },
   )

