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