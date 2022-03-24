from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'


class Dish(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'dishes'


class Topping(models.Model):
    title = models.CharField(max_length=100)


class DishTopping(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)


class SizeType(models.Model):
    title = models.CharField(max_length=100)


class DishSize(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    size_type = models.ForeignKey(SizeType, on_delete=models.CASCADE)
    size_value = models.FloatField
    weight = models.FloatField
    price = models.PositiveIntegerField
