import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'article_web_app.settings')
import django

django.setup()
from article_reviewer.models import Category, Article, Review, User, UserProfile


def add_cat(name, picture):
    c = Category.objects.get_or_create(name=name, picture=picture)[0]
    c.save()
    return c


def add_article(cat, title, url, picture, author="Unknown", AvgRating=3, Review="", totalRating=0, AmountOfRatings=0):
    A = Article.objects.get_or_create(category=cat, title=title, url=url, picture=picture, author=author,
                                      averageRating=AvgRating, reviews=Review, totalRating=totalRating, amountOfRatings=AmountOfRatings)[0]
    A.url = url
    A.save()
    return A
    


##populate fuction 
def populate():
    ##
    ##img src="C:\Users\user\Workspace\new_project\article-web-app\static\article.png" alt="Picture of article" />
    ##{'title': '','url': '','author': '', 'picture': ''}

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
    politics_articles = []
    science_articles = [{'title': 'Elon Musk’s SpaceX becomes first private company to launch a reused rocket ','url': 'https://www.cnbc.com/2017/12/15/elon-musks-spacex-becomes-first-to-launch-reused-rocket-on-a-nasa-mission.html','author': 'Michael Sheetz', 'picture': 'article_images/elon.png'}]
    nature_articles = [{'title': 'Octopus Facts','url': 'https://www.livescience.com/55478-octopus-facts.html#:~:text=Octopuses%20are%20ocean%20creatures%20that%20are%20most%20famous,quite%20intelligent%20and%20have%20been%20observed%20using%20tools.','author': ' Alina Bradford', 'picture': 'article_images/octopus.png'}]
    news_articles = []
    celebrity_articles = [{'title': 'Laura Whitmore unveils jaw-dropping party trick','url': 'https://www.mirror.co.uk/3am/celebrity-news/laura-whitmore-unveils-jaw-dropping-23862112','author': 'Tamara Davison', 'picture': 'article_images/partytrick.png'}]
    health_articles = [{'title': 'The 14 Healthiest Vegetables on Earth','url': 'https://www.healthline.com/nutrition/14-healthiest-vegetables-on-earth','author': ' Rachael Link', 'picture': 'article_images/healthline.png'},
    {'title': '20 Healthy and Energizing Snacks','url': 'https://www.healthline.com/nutrition/healthy-energizing-snacks#9.-Premade-guacamole-and-plantain-chips','author': ' Jillian Kubala', 'picture': 'article_images/healthysnacks.png'}]

    # cartegories
    cats = {'History': {'articles': history_articles, 'picture': 'category_images/HistoryImage.png'}, 'Music': {'articles': music_articles, 'picture': 'category_images/MusicImage.jpg'},
            'Sport': {'articles': sports_articles, 'picture': 'category_images/SportImage.jpg'}, 'Film': {'articles': film_articles, 'picture': 'category_images/FilmImage.jpg'}, 
            'Politics' : {'articles': politics_articles, 'picture': 'category_images/PoliticsImage.jpg'}, 'Science' : {'articles': science_articles, 'picture': 'category_images/ScienceImage.jpg'},
            'Nature' : {'articles': nature_articles, 'picture': 'category_images/NatureImage.jpg'}, 'News' : {'articles': news_articles, 'picture': 'category_images/NewsImage.jpg'}, 
            'Celebrity' : {'articles': celebrity_articles, 'picture': 'category_images/CelebrityImage.jpeg'}, 'Health' : {'articles' : health_articles, 'picture' : 'category_images/HealthImage.jpg'}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['picture'])
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
