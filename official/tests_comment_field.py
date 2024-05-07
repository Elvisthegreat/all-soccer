from django.test import TestCase
from .forms import CommentForm

# Create your tests here.
class TestCommentForm(TestCase):
    def test_comment_form_is_valid(self):
        comment_form = CommentForm({'body': 'Football is best sport'})

        """using an assertTrue to determine if the form is valid. 
           Since the body field is required"""
        self.assertTrue(comment_form.is_valid(), msg='Comment form is not valid')

    def test_comment_form_is_not_valid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg='Comment form is valid')
