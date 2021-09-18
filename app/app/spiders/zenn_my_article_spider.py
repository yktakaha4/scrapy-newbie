import scrapy
from scrapy.http.response import Response
from app.items import ZennArticlesItem

class ZennMyArticleSpiderSpider(scrapy.Spider):
    name = 'zenn_my_article_spider'
    allowed_domains = ['zenn.dev']
    start_urls = ['http://zenn.dev/yktakaha4']

    def parse(self, response: Response):
        for article in response.css('*[class*="ArticleCard_container__"]'):
            yield ZennArticlesItem(
                url = article.css('*[class*="ArticleCard_mainLink__"]').attrib.get('href'),
                article_type = article.css('*[class*="ArticleCard_category__"]::text').extract_first(),
                title = article.css('*[class*="ArticleCard_title__"]::text').extract_first(),
                likes = article.css('*[class*="ArticleCard_like__"]::text').getall()[-1],
                date = article.css('*[class*="ArticleCard_meta__"] > time').attrib.get('datetime'),
            )
