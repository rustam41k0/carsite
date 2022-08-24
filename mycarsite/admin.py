from django.contrib import admin

from mycarsite.models import *


# class PostsAdmin(admin.ModelAdmin):
#     list_filter = ('main_title',)
#     prepopulated_fields = {'slug': ('main_title',)}


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
admin.site.register(Posts) # , PostsAdmin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments)
admin.site.register(Tags, TagsAdmin)

#   Limousine
# 	Cabriolet
# 	Sportcar
# 	Hatchback
# 	Sedan
# 	Pickup
# 	Off-road
# 	Сrossover
