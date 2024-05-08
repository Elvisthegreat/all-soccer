from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm
from .models import ContactUs

class ContactUsFormView(TestCase):

    """ Testing views with GET """
    def setUp(self):
        """Creates contact us content"""
        self.contact_us = ContactUs(
            title="Contact us", content="Reach out to us.")
        self.contact_us.save()

    

    def test_render_contact_page_with_contact_us_form(self):
        """Verifies get request for containing contact us form"""
        # The reverse('contact') point to the name of our urls.py
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Us', response.content)
        self.assertIsInstance(
            response.context['contact_form'], ContactForm)


    def test_contact_us_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'Elvis blessing',
            'email': 'elvis@6gmail.com',
            'message': 'Hello am curious to know about all football'
        }
        response = self.client.post(reverse('contact'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Thanks for filling out the form, one of our creators will get back to you",
            response.content
        
        )