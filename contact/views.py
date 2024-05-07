from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import ContactUs
from .forms import ContactForm

# Create your views here.
def contact(request):

    contact = ContactUs.objects.all()
    contact_form = ContactForm()

    """ Handling the About section form request """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Thanks for filling out the form, one of our creators will get back to you"
            )

    coontact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
            "contact_form": contact_form,
        }
    )