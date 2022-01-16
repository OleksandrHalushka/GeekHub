# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import csv

import self as self

from .spiders import vikkanewsscrape
import pathlib
import os
from scrapy.exporters import CsvItemExporter
from itemadapter import ItemAdapter


def write_to_csv(item):
    file = open(f"{item['date']}.csv", 'a', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([item[key] for key in item.keys()])


class GeekHubPipeline:

    def process_item(self, item, spider):
        write_to_csv(item)
        return item
