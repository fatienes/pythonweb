from django.contrib import admin

# Register your models here.
from .models import Auther
from .models import Book

admin.site.register(Auther)
admin.site.register(Book)
