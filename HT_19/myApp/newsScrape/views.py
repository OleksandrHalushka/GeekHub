from django.shortcuts import render
from .forms import CategoryForm
from .models import *
from .models import Askstory, Showstory, Jobstory, Newstory, News
import requests


class NewsFromApi(object):
    categories = {
        'askstories': Askstory,
        'showstories': Showstory,
        'newstories': Newstory,
        'jobstories': Jobstory
    }

    def __init__(self, category):
        self.category = category

    def get_news(self):
        url = f'https://hacker-news.firebaseio.com/v0/{self.category}.json'
        articles = requests.get(url).json()
        object_category = self.categories[self.category]()

        for article in articles:
            try:
                news = News.objects.get(id=article).exists()

            except:
                url = f'https://hacker-news.firebaseio.com/v0/item/{article}.json'
                answer = requests.get(url=url).json()
                if not answer:
                    continue
                else:

                    object_category.id = answer.get("id")
                    object_category.by = answer.get("by")
                    object_category.descendants = answer.get("descendants")
                    object_category.score = answer.get("score")
                    object_category.text = answer.get("text")
                    object_category.time = answer.get("time")
                    object_category.title = answer.get("title")
                    object_category.type = answer.get("type")
                    object_category.url = answer.get("url")
                    news = News()
                    news.id = answer.get("id")
                    object_category.save()
                    news.save()


def index(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            news_from_api = NewsFromApi(category)
            news_from_api.get_news()
            return render(request, 'index_done.html')
    else:
        form = CategoryForm()
        return render(request, 'index.html', {"form": form})
