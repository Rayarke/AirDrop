from itemadapter import ItemAdapter
from scrapy.item import Item
from scrapy.exceptions import DropItem
import os


class TutorialPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('title') is None:
            DropItem(adapter.get('title'))
        if adapter.get('content') is None:
            DropItem(adapter.get('content'))
        filename = '/Users/lambs/PycharmProjects/victor/tutorial/tutorial/spiders/item.txt'
        with open(filename, 'a') as f:
            f.write(item['title'] + '\n')
            f.write(item['content'] + '\n')
        return item
