from django.shortcuts import render, get_object_or_404
from django.http import Http404
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

# def club_history(request, slug):
#     """
#     View function to display football club history based on the club name.
#     :param request: HTTP request
#     :param slug: Unique identifier for the football club
#     :param club_name: Name of the football club (e.g., 'barcelona', 'psg', etc.)
#     :return: Rendered template with relevant data
#     """
#     queryset = Football.objects.all()
#     ball = get_object_or_404(queryset, slug=slug)

#     # Dictionary mapping slugs to template names
#     templates = {
#         'barcelona': 'football/barcelona_history.html',
#         'psg': 'football/psg_history.html',
#         'real_madrid': 'football/real_madrid_history.html',
#         'man_city': 'football/man_city_history.html',
#     }

#     # If the slug is not found in the templates dictionary, raise a 404 error
#     if slug not in templates:
#         raise Http404("No template found for the given slug.")
#     template = templates[slug]

#     return render(
#         request, template,
#         {
#             'ball': ball,
#         },
#     )
