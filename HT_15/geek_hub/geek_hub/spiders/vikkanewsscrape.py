from requests import Request

import scrapy
import datetime

from ..items import VikkaNewsItem

from bs4 import BeautifulSoup


class LaterDate(Exception):
    pass


class VikkaNewsScrapeSpider(scrapy.Spider):
    name = 'vikkanewsscrape'
    allowed_domains = ['vikka.ua']
    start_urls = ['https://www.vikka.ua/category/novini/']

    def create_date(self):
        date = input('Please, input date like: dd_mm_yyyy): ')
        try:
            date = datetime.datetime.strptime(date, '%d_%m_%Y')
            print(date)
            if date > datetime.datetime.today():
                raise LaterDate()
            else:
                date = date.strftime('%Y_%m_%d')
                return date
        except LaterDate:
            print('Inputted date is later than today!')
        except ValueError:
            print('Wrong date')

    def start_requests(self):
        date = self.create_date()
        url = f'http://vikka.ua/{"/".join(date.split("_"))}/'
        yield scrapy.Request(
            url=url,
            callback=self.parse_page,
            cb_kwargs=dict(name=f'{date}')
        )

    def parse_page(self, response, name):
        soup = BeautifulSoup(response.text, "lxml")
        for news in soup.select('.title-cat-post a'):
            urls = news.get('href')
            yield scrapy.Request(
                url=urls,
                callback=self.parse_news,
                cb_kwargs=dict(name=name)
            )

        next_page_url = soup.select_one('.nav-links a.next.page-numbers')
        if not next_page_url:
            return
        yield scrapy.Request(
            url=next_page_url.get('href'),
            callback=self.parse_news,
            cb_kwargs=dict(name=name)
        )

    def parse_news(self, news, name):
        article = ''
        soup = BeautifulSoup(news.text, "lxml")
        items = VikkaNewsItem()
        items['title'] = soup.select_one('h1.post-title').text
        for string in soup.select_one('.entry-content'):
            article += f'{string.text}\n'
        items['article'] = article
        items['tags'] = ', '.join([f'#{i.text}' for i in soup.select('.post-tag')])
        items['url'] = news.url
        items['date'] = name

        return items
