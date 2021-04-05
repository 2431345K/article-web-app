import os
import warnings
import importlib
from django.test import TestCase
from article_reviewer.models import Category, Article, Review, UserProfile
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class ModelTests(TestCase):
    """
    Are the models set up correctly?
    """
    def create_user_object(self):
        user = User.objects.get_or_create(username='testuser', first_name='Test', last_name='User', email='test@test.com')[0]
        user.set_password('testabc123')
        user.save()
        return user
    
    def setUp(self):
        category = Category.objects.get_or_create(name='Science', slug=slugify('Science'))
        article = Article.objects.get_or_create(category=category, url='/category/example_title', author='example', averageRating=3, reviews=None, title='example_title')
        review = Review.objects.get_or_create(article=article, commentID=123, rating=4, author='example', date='2021-04-05', comment='This is an example comment')
        user_profile = UserProfile.objects.get_or_create(user=self.create_user_object, picture=None, author=False)
        

    def test_category_class(self):
        category = Category.objects.get(name='Science')
        self.assertEqual(category.name, 'Science', f"{FAILURE_HEADER}Tests on the Category model failed.{FAILURE_FOOTER}")
        self.assertEqual(category.slug, slugify('Science'), f"{FAILURE_HEADER}Tests on the Category model failed.{FAILURE_FOOTER}")

    def test_article_class(self):
        article = Article.objects.get_or_create(url='/category/example_title')
        self.assertEqual(article.category, Category.objects.get(name='Science'), f"{FAILURE_HEADER}Tests on the Article model failed.{FAILURE_FOOTER}")
        self.assertEqual(article.url, '/category/example_title', f"{FAILURE_HEADER}Tests on the Article model failed.{FAILURE_FOOTER}")
        self.assertEqual(article.author, 'example', f"{FAILURE_HEADER}Tests on the Article model failed.{FAILURE_FOOTER}")
        self.assertEqual(article.averageRating, 3, f"{FAILURE_HEADER}Tests on the Article model failed.{FAILURE_FOOTER}")
        self.assertEqual(article.title, 'example_title', f"{FAILURE_HEADER}Tests on the Article model failed.{FAILURE_FOOTER}")

    def test_review_class(self):
        review = Review.objects.get_or_create(commentID=123)
        self.assertEqual(review.article, Article.objects.get_or_create(url='/category/example_title'), f"{FAILURE_HEADER}Tests on the Review model failed.{FAILURE_FOOTER}")
        self.assertEqual(review.commentID, 123, f"{FAILURE_HEADER}Tests on the Review model failed.{FAILURE_FOOTER}")
        self.assertEqual(review.rating, 4, f"{FAILURE_HEADER}Tests on the Review model failed.{FAILURE_FOOTER}")
        self.assertEqual(review.author, 'example', f"{FAILURE_HEADER}Tests on the Review model failed.{FAILURE_FOOTER}")
        self.assertEqual(review.date, '2021-04-05', f"{FAILURE_HEADER}Tests on the Review model failed.{FAILURE_FOOTER}")
        self.assertEqual(review.comment, 'This is an example comment', f"{FAILURE_HEADER}Tests on the Review model failed.{FAILURE_FOOTER}")

    def test_userprofile_class(self):
        user_profile = UserProfile.objects.get_or_create(user=self.create_user_object)
        self.assertEqual(user_profile.user, self.create_user_object, f"{FAILURE_HEADER}Tests on the User Profile model failed.{FAILURE_FOOTER}")
        self.assertEqual(user_profile.picture, None, f"{FAILURE_HEADER}Tests on the User Profile model failed.{FAILURE_FOOTER}")
        self.assertEqual(user_profile.author, False, f"{FAILURE_HEADER}Tests on the User Profile model failed.{FAILURE_FOOTER}")


