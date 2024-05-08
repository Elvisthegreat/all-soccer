from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Official

# Create your tests here.
class TestOfficialViews(TestCase):

    def setUp(self):
        """ Testing views with GET """
        """ A small setup model for testing """
        self.user = User.objects.create_superuser(
            username='elvis',
            password='elvisPassword',
            email='elvis6@gmail.com'
        )
        self.ball = Official(title="Official title", author=self.user,
                         slug="official-title", excerpt="Official excerpt",
                         content="Official content")
        self.ball.save()

    def test_render_official_news_page_with_comment_form(self):
        """ Testing views with GET """
        response = self.client.get(reverse(
            'official_news', args=['official-title']))
        self.assertEqual(response.status_code, 200)

        """checks whether the first argument (in this case, "Blog title")
           is present in the second argument (in this case, response.content)"""
        self.assertIn(b"Official title", response.content)
        self.assertIn(b"Official content", response.content)

        """Verifies that the comment_form from
           the post_detail view's context is an
           instance of the CommentForm class."""
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)


    def test_comment_submission_if_successful(self):
        """Test for posting a comment on a post"""
        self.client.login(username="elvis", password="elvisPassword")
        post_data = {
            'body': 'A simple testing comment.'
        }
        response = self.client.post(
            reverse('official_news', args=['official-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted successful',
            response.content)