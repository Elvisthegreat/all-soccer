# Imports & 3rd party imports
from django.contrib import admin
from .models import ContactUs


# Registraion of the users contact information in the admin panel
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)