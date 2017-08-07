from django.contrib import admin
from .models import Phone
from .models import Extension

admin.site.register(Phone)
admin.site.register(Extension)
