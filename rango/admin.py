from django.contrib import admin
from rango.models import Category, Page , UserProfile

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
