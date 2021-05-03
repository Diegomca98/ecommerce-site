from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, verbose_name="Product")
    product_price = models.FloatField(verbose_name="Price")
    discount_price = models.FloatField(verbose_name="Discount Price")
    category = models.CharField(max_length=200, verbose_name="Brand")
    product_description = models.TextField(verbose_name="Description")
    product_image = models.CharField(max_length=500, verbose_name="Image")
    prdocut_sku = models.CharField(max_length=100, verbose_name="SKU")
    product_availability = models.BooleanField(verbose_name="In Stock")
    has_discount = models.BooleanField(verbose_name="¿Has Discount?", default=False)
    

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name

class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=1000, verbose_name="Items Ordered")
    name = models.CharField(max_length=200, verbose_name="Customer Name")
    last_name = models.CharField(max_length=200, verbose_name="Customer Last Name")
    email = models.CharField(max_length=200, verbose_name="Customer Email")
    address = models.CharField(max_length=200, verbose_name="Customer Address")
    address2 = models.CharField(max_length=200, verbose_name="Customer Apartment")
    country = models.CharField(max_length=200, verbose_name="Country")
    state = models.CharField(max_length=200, verbose_name="State")
    zip_code = models.CharField(max_length=200, verbose_name="Zip Code")
    total = models.FloatField(max_length=200, verbose_name="Order Total", default=0)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ("id", "name", "last_name")
    
    def __str__(self):
        return f"Order No.{self.id} - {self.name} {self.last_name}"
    