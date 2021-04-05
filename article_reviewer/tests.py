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
        article = Article.objects.get_or_create(category=str(category), url='/category/example_title', author='example', averageRating=3, reviews=None, title='example_title')
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


class SettingsTests(TestCase):
    """
    is Settings set up correctly?
    """
    def test_variable_existance(self):
        self.assertTrue(settings.DATABASES, f"{FAILURE_HEADER}settings.py does not have a DATABASES variable.{FAILURE_FOOTER}")
        self.assertTrue(settings.INSTALLED_APPS, f"{FAILURE_HEADER}settings.py does not have an INSTALLED_APPS variable.{FAILURE_FOOTER}")
        self.assertTrue(settings.MIDDLEWARE, f"{FAILURE_HEADER}settings.py does not have a MIDDLEWARE variable.{FAILURE_FOOTER}")
        self.assertTrue(settings.TEMPLATES, f"{FAILURE_HEADER}settings.py does not have a TEMPLATES variable.{FAILURE_FOOTER}")
        self.assertTrue(settings.AUTH_PASSWORD_VALIDATORS, f"{FAILURE_HEADER}settings.py does not have a AUTH_PASSWORD_VALIDATORS variable.{FAILURE_FOOTER}")
        self.assertTrue(settings.STATIC_URL, f"{FAILURE_HEADER}settings.py does not have a STATIC_URL variable.{FAILURE_FOOTER}")
        self.assertTrue(settings.MEDIA_URL, f"{FAILURE_HEADER}settings.py does not have a MEDIA_URL variable.{FAILURE_FOOTER}")
    

class PopulationScriptTests(TestCase):
    """
    Does the population script work correctly?
    """
    def test_categories(self):

        categories = Category.objects.all()
        categories_len = len(categories)
        categories_strs = map(str, categories)

        self.assertEqual(categories_len, 4, f"{FAILURE_HEADER}Expecting 4 categories to be created from the populate_article_reviewer module; found {categories_len}.{FAILURE_FOOTER}")
        self.assertTrue('History' in categories_strs, f"{FAILURE_HEADER}The category 'History' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
        self.assertTrue('Music' in categories_strs, f"{FAILURE_HEADER}The category 'Music' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
        self.assertTrue('sport' in categories_strs, f"{FAILURE_HEADER}The category 'sport' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
        self.assertTrue('film' in categories_strs, f"{FAILURE_HEADER}The category 'film' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
    
    def test_articles(self):
        
        articles = Article.objects.all()
        articles_len = len(articles)
        articles_strs = map(str, articles)

        self.assertEqual(articles_len, 5, f"{FAILURE_HEADER}Expecting 4 categories to be created from the populate_article_reviewer module; found {articles_len}.{FAILURE_FOOTER}")
        self.assertTrue('https://www.espn.com/mma/story/_/id/31149463/ufc-260-francis-ngannou-won-ufc-heavyweight-championship-jon-jones-superfight-awaits' in articles_strs, f"{FAILURE_HEADER}The article 'Ngannou new champ' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
        self.assertTrue('https://www.onthisday.com/articles/the-man-who-saved-elton-johns-life' in articles_strs, f"{FAILURE_HEADER}The article 'The Man Who Saved Elton Johns Life' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
        self.assertTrue('https://www.billboard.com/hub/legal-and-management/' in articles_strs, f"{FAILURE_HEADER}The article 'ticketmaster sued' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
        self.assertTrue('https://www.billboard.com/video/ariana-grande-transforms-into-a-robot-for-futuristic-3435-music-video-billboard-news' in articles_strs, f"{FAILURE_HEADER}The article 'Ariana Grande Transforms Into a Robot For Futuristic 34+35' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")
        self.assertTrue('https://observer.com/2021/04/justice-league-hbo-max-ratings-viewership-subscribers-netflix-disneyplus-amazon/' in articles_strs, f"{FAILURE_HEADER}The article 'justice league' was expected but not created by populate_article_reviewer.{FAILURE_FOOTER}")


class InterfaceTests(TestCase):
    
    def setUp(self):
        """
        Create a superuser account for use in testing.
        Logs the superuser in, too!
        """
        User.objects.create_superuser('testAdmin', 'email@email.com', 'adminPassword123')
        self.client.login(username='testAdmin', password='adminPassword123')
        
        category = Category.objects.get_or_create(name='TestCategory')[0]
        Article.objects.get_or_create(title='TestPage1', url='https://www.google.com', category=category, author='example', averageRating=3)
    
    def test_admin_interface_accessible(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}The admin interface is not accessible.{FAILURE_FOOTER}")
    
    def test_models_present(self):
        """
        Checks whether the two models are present within the admin interface homepage -- and whether Rango is listed there at all.
        """
        response = self.client.get('/admin/')
        response_body = response.content.decode()
        
        # Is the Rango app present in the admin interface's homepage?
        self.assertTrue('Models in the Rango application' in response_body, f"{FAILURE_HEADER}The Rango app wasn't listed on the admin interface's homepage. You haven't added the models to the admin interface.{FAILURE_FOOTER}")
        
        # Check each model is present.
        self.assertTrue('Categories' in response_body, f"{FAILURE_HEADER}The Category model was not found in the admin interface.{FAILURE_FOOTER}")
        self.assertTrue('Articles' in response_body, f"{FAILURE_HEADER}The Article model was not found in the admin interface.{FAILURE_FOOTER}")
