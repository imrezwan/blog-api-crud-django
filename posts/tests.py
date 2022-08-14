from django.test import TestCase
from .models import User, Post

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        #create user
        test_user1 = User.objects.create_user(
            username = 'testuser1',
            password = 'testpass',
        )
        test_user1.save()
        #create blogpost
        test_post = Post.objects.create(
            author = test_user1,
            title = 'First Blog',
            body = 'Blog Details Here',
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'First Blog')
        self.assertEqual(body, 'Blog Details Here')