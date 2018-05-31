from django.contrib import admin

# Register your models here.
from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'linenos', 'language', 'style']


admin.site.register(Snippet, SnippetAdmin)
