from django.contrib import admin
from .models import Post


# About Django admin site   https://docs.djangoproject.com/en/4.1/ref/contrib/admin/

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}  # automatically filled the slug field from title
    raw_id_fields = ['author']  # author field displayed with a lookup widget
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
