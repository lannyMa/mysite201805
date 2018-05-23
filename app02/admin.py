from django.contrib import admin

# Register your models here.
from app02.models import Publish, Author, Book

admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(Book)
