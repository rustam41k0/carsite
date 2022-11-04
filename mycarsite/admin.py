from django.contrib import admin

from mycarsite.models import *


class CarsAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class TagsAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cars, CarsAdmin)
admin.site.register(Posts)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments)
admin.site.register(Tags, TagsAdmin)