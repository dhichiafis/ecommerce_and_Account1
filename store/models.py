from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=123)
    slug=models.SlugField(max_length=123)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_detail',args=[self.slug])

class Product(models.Model):
    name=models.CharField(max_length=123)
    slug=models.SlugField(max_length=123)
    body=models.TextField()
    image=models.ImageField(upload_to='images')
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail',args=[self.slug])

class Order(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=123)
    total_cost=models.IntegerField(default=0)
    is_paid=models.BooleanField(default=False)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='item',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='item',on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField(default=0)
