from django.db import models

# Create your models here.

class ItemCategory(models.Model):
    
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Item Category"
        verbose_name_plural = "Item Categories"


class Item(models.Model):
    itemName = models.CharField(max_length=50)
    slug = models.SlugField(default="")
    description = models.CharField(max_length=50)
    itemCategory = models.ForeignKey( ItemCategory, on_delete=models.CASCADE, related_name="item")
    image = models.ImageField(upload_to="image")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.itemName}"




class OrderDetail(models.Model):
    item = models.ForeignKey( Item ,null=True, on_delete=models.SET_NULL, related_name="orderItem")
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(default=0)

class Order(models.Model):
    username = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    order_detail = models.ManyToManyField(OrderDetail)
    grand_total = models.DecimalField( max_digits=5, decimal_places=2)