import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'article_web_app.settings')
import django

django.setup()
from article_reviewer.models import Category, Article, Review, User, UserProfile


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_article(cat, title, url, picture, author="Unknown", AvgRating=5, Review=""):
    A = Article.objects.get_or_create(category=cat, title=title, url=url, picture=picture, author=author,
                                      averageRating=AvgRating, reviews=Review)[0]
    A.url = url
    A.save()
    return A
    


##populate fuction 
def populate():
    ##
    ##img src="C:\Users\user\Workspace\new_project\article-web-app\static\article.png" alt="Picture of article" />
    ##

    sports_articles = [{'title': 'Ngannou new champ',
                        'url': 'https://www.espn.com/mma/story/_/id/31149463/ufc-260-francis-ngannou-won-ufc-heavyweight-championship-jon-jones-superfight-awaits',
                        'author': 'ESPN', 'picture': 'article_images/ngannou.png'}]
    history_articles = [{'title': 'The Man Who Saved Elton Johns Life',
                         'url': 'https://www.onthisday.com/articles/the-man-who-saved-elton-johns-life',
                         'author': 'Ray Setterfield', 'picture': 'article_images/elton.png'}]
    music_articles = [{'title': 'ticketmaster sued ', 'url': 'https://www.billboard.com/hub/legal-and-management/',
                       'author': 'Dave Brooks', 'picture': 'article_images/ticketmaster.png'},
                      {'title': 'Ariana Grande Transforms Into a Robot For Futuristic 34+35',
                       'url': 'https://www.billboard.com/video/ariana-grande-transforms-into-a-robot-for-futuristic-3435-music-video-billboard-news',
                       'author': 'BillBoard News', 'picture': 'article_images/arianarobot.png'}]
    film_articles = [{'title': 'justice league',
                      'url': 'https://observer.com/2021/04/justice-league-hbo-max-ratings-viewership-subscribers-netflix-disneyplus-amazon/',
                      'author': 'Observer', 'picture': 'article_images/justiceleague.png'}]

    # cartegories
    cats = {'History': {'articles': history_articles}, 'Music': {'articles': music_articles},
            'sport': {'articles': sports_articles}, 'film': {'articles': film_articles}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['articles']:
            add_article(c, p['title'], p['url'], p['picture'], p['author'])


    # Print out the categories we have added.
    for c in Category.objects.all():
        for a in Article.objects.filter(category=c):
            print(f'- {c}: {a}')


# Start execution here!
if __name__ == '__main__':
    print('Starting article_reviewer population script...')
    populate()
