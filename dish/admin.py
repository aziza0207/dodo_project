from django.contrib import admin

from .models import *
admin.site.register(Dish)
admin.site.register(DishSize)
admin.site.register(SizeType)
admin.site.register(Topping)
admin.site.register(DishTopping)
admin.site.register(Category)

