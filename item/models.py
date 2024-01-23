from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from datetime import timedelta



class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images', blank=True, null=True)


    class Meta:
        ordering = ("name",)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name = 'items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True, null = True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_rent = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name = 'items', on_delete = models.CASCADE)
    rented_by = models.ForeignKey(User, related_name = 'rented_items', on_delete=models.SET_NULL, null=True, blank=True)
    rented_at = models.DateTimeField(blank=True, null=True)
    
    def is_rented_for_more_than_24_hours(self):
        if self.rented_at:
            return timezone.now() - self.rented_at > timedelta(hours=24)
        return False
    
    def __str__(self):
        return self.name


class ItemDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.item.price
        super(ItemDetail, self).save(*args, **kwargs)

    def __str__(self):
        return f"Detail of {self.item.name}"