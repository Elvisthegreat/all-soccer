from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactUs
from .forms import ContactForm

def contact(request):
    contact = ContactUs.objects.all()
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Thanks for filling out the form, one of our creators will get back to you"
            )
            return redirect('contact')

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
            "contact_form": contact_form,
        }
    )
