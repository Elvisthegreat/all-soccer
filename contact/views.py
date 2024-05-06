from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact(request):

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
        }
    )