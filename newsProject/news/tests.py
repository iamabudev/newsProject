from django.test import TestCase
from django.urls import reverse
from .models import  Post

class PostModeTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Theme', text='news text')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_title=f'{post.title}'
        expected_object_text=f'{post.text}'
        self.assertEqual(expected_object_title,'Theme')
        self.assertEqual(expected_object_text,'news text')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Theme 2', text='other news')

    def test_views_url_exists_at_proper_location(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_template(self):
        resp=self.client.get(reverse('home'))

