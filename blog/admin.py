from django.contrib import admin

# Register your models here.
from .models import Blog
admin.site.register(Blog) #어드민 사이트에 등록