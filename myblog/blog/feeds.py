import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')  # Генерирует URL-адреса по их имени и передает опциональные параметры
    description = 'New posts of my blog.'

    def items(self):  # Извлекает включаемые в новостную ленту объекты
        return Post.published.all()[:5]

    def item_title(self, item):  # Функция для вывода заголовка новости
        return item.title

    def item_description(self, item):  # Функция для вывода описания новости
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):  # Функция для вывода даты новости
        return item.publish