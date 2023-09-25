from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'  # Частота изменения страниц постов
    priority = 0.9  # Приоритетность страниц постов

    def items(self):  # Возвращает QuerySet объектов, подлежащих включению в карту сайта
        return Post.published.all()

    def lastmod(self, obj):  # Получает дату последнего изменения объекта из items()
        return obj.updated
