from django.contrib import admin

# Register your models here.
from app01.models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'nick_name', 'add_time']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'add_time', ]
    search_fields = ['title', 'category', ]
    list_filter = ['title', 'category', 'add_time', ]
    list_display_links = None
    list_editable = ['title', 'category', ]
    filter_horizontal = ['tag', ]
    list_per_page = 2
    ordering = ('-add_time',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
