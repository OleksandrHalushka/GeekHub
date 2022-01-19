# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
import pathlib


class GeekHubPipeline:
    conn = sqlite3.connect("news.db")
    cur = conn.cursor()

    def open_spider(self, spider):
        conn = sqlite3.connect("news.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS news(
                       id INTEGER PRIMARY KEY,
                       title TEXT,
                       article TEXT,
                       tags TEXT,
                       url TEXT,
                       date TEXT)""")
        self.conn.commit()

    def process_item(self, item, spider):

        item_tuple = (item[key] for key in item.keys())
        self.cur.execute("""INSERT INTO news(title, article, tags, url, date) VALUES(?,?,?,?,?);""", tuple(item_tuple))

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
