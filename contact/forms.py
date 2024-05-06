from .models import ContactUs
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+3935190768745'}))


    class Meta:
        model = ContactUs
        fields = '__all__'  # Include all fields from the model except the "read" field
        exclude = ['read']  # Exclude the "read" field from the form