from django.contrib import admin

from dish.models import *


class DishAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


class ToppingAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Dish, DishAdmin)
admin.site.register(DishSize)
admin.site.register(SizeType)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(DishTopping)
admin.site.register(Category, CategoryAdmin)
