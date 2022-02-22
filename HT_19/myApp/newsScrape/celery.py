import logging
import requests
import os

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .models import Newstory, Askstory, Jobstory, Showstory
from celery import app


def get_ids_list(category):
    url = f'https://hacker-news.firebaseio.com/v0/{category}.json'
    articles_list = requests.get(url=url).json()
    return articles_list

@app.task
def get_news_csv(category):
    ids_list = [obj.id for obj in Newstory.objects.all()]
    ids_list.append([i.id for i in Askstory.objects.all()])
    ids_list.append([i.id for i in Jobstory.objects.all()])
    ids_list.append([i.id for i in Showstory.objects.all()])

    curent_models = {'newstories': Newstory(), 'askstories': Askstory(), 'jobstories': Jobstory(), 'showstories': Showstory()}
    news = curent_models[category]

    list_of_articles = get_ids_list(category)

    for article in list_of_articles:
        if Askstory.objects.filter(id=article).count() != 0 \
                or Showstory.objects.filter(id=article).count() != 0 \
                or Newstory.objects.filter(id=article).count() != 0 \
                or Jobstory.objects.filter(id=article).count() != 0:
            continue

        temp_url = f'https://hacker-news.firebaseio.com/v0/item/{i}.json'
        c_request = requests.get(url=temp_url).json()

        if not c_request:
            continue

        for k, v in c_request.items():
            setattr(news, k, v)
            news.save()
    return