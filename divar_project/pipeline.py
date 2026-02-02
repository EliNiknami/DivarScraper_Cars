# Define your item pipelines here

# Don't forget to add your pipeline to the ITEM_PIPELINES setting

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DivarProjectPipeline:
    def process_item(self, item, spider):
        return item
