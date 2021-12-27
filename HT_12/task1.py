"""
http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в репозиторії.
Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL). Хто захардкодить
пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)
"""
import sqlite3
from bs4 import BeautifulSoup
import requests
import datetime
import csv


def parser():
    root_url = 'https://quotes.toscrape.com/'
    url = root_url
    authors = []
    quote_list = []
    authors_list = []
    quote_id = 1
    author_id = 1
    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        for quote in soup.select('.quote'):
            text = quote.select('.text')[0].text.strip('“”')
            author = quote.select('.author')[0].text
            quote_list.append([quote_id, text, author])
            quote_id += 1
            if author not in authors:
                authors.append(author)
                about_link = root_url + quote.select('a')[0].get('href')
                author_page = requests.get(about_link)
                author_soup = BeautifulSoup(author_page.text, 'lxml')
                was_born = author_soup.select('.author-born-date')[0].text
                was_born = datetime.datetime.strptime(was_born, '%B %d, %Y').date()
                place_born = author_soup.select('.author-born-location')[0].text[3:]
                description = author_soup.select('.author-description')[0].text
                authors_list.append([author_id, author, was_born, place_born, description])
                author_id += 1
        if soup.select('.next'):
            next_page = soup.select('.next a')
            link = next_page[0].get('href')
            url = root_url + link
        else:
            break

    with open('authors.csv', 'w', encoding="utf-8") as authors_file:
        authors_writer = csv.writer(authors_file)
        authors_writer.writerow(('Id', 'Name', 'Was_born', 'Place', 'About'))
        authors_writer.writerows(authors_list)

    with open('quotes.csv', 'w', encoding="utf-8") as quote_file:
        quote_writer = csv.writer(quote_file)
        quote_writer.writerow(('Id', 'Quote', 'Author'))
        quote_writer.writerows(quote_list)

    fop = open('quotes.db', 'w')
    fop.close()
    conn = sqlite3.connect('quotes.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS quotes(
                   quote_id INT PRIMARY KEY,
                   text TEXT,
                   author TEXT)""")
    cur.executemany("""INSERT INTO quotes VALUES(?,?,?);""", quote_list)
    cur.execute("""CREATE TABLE IF NOT EXISTS authors (
           author_id INT PRIMARY KEY,
           name TEXT,
           was_born TEXT,
           place_born TEXT,
           description TEXT)""")
    cur.executemany("""INSERT INTO authors VALUES(?,?,?,?,?);""", authors_list)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    parser()
