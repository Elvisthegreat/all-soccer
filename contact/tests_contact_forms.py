from django.test import TestCase
from .forms import ContactForm

# Create your tests here.
class TestContactForm(TestCase):

    def test_contact_form_is_valid(self):
        """Testing all fields"""
        contact = ContactForm({
            'name': 'Elvis',
            'email': 'elvis6@gmail.com',
            'phone': '+393510476952',
            'message': 'Hello Elvis'
        })
        self.assertTrue(contact.is_valid(), msg='Form contact is not valid')

    def test_form_contact_is_valid_one(self):
        """check that the form is not valid if we fail 
        to populate one of the fields in the dictionary."""

        contact_one = ContactForm({
            'name': '',
            'email': 'elvis6@gmail.com',
            'phone': '+393510476952',
            'message': 'Hey!'
        })
        self.assertFalse(contact_one.is_valid(), msg="Form contact is not correctly populated")

    def test_form_contact_is_valid_two(self):
        """check that the form is not valid if we fail 
        to populate one of the fields in the dictionary."""

        contact_two = ContactForm({
            'name': 'Blessing',
            'email': 'test@amadin.com',
            'phone': '',
            'message': 'Yeah!'
        })
        self.assertFalse(contact_two.is_valid(), msg='Form contact is not correctly populated')
