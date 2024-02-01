from django.contrib import admin
from .models import Category,Blog


class BlogHome(admin.ModelAdmin):
    list_display=["book_name","writer","homepage","best","active"]
    list_editable=["homepage","best","active"]
    list_filter=["category","active"]

admin.site.register(Category)
admin.site.register(Blog,BlogHome)
# Register your models here.