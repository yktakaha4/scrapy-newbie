# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from app.models import ZennArticlesModel
from itemadapter import ItemAdapter
from app.items import ZennArticlesItem
from datetime import datetime


class AppPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if adapter.is_item_class(ZennArticlesItem):
            url = item['url']
            model, created = ZennArticlesModel.get_or_create(
                url=url,
                defaults={
                    'article_type': 'piyo',
                    'title': 'title',
                    'likes': 0,
                    'date': datetime.now()
                },
            )
            if not created:
                model.article_type = 'piyo'
                model.title = 'title'
                model.likes = 0
                model.date = datetime.now()

                model.save()

        return item
