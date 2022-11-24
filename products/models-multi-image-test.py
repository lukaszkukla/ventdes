from django.db import models
from django.core.validators import MinLengthValidator


class Category(models.Model):
    """
    Category class
    """
    class Meta:
        """
        Meta class for Category
        """
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product class
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(
        max_digits=1, null=True, blank=True
    )
    image = models.ForeignKey(
        'ProductImage', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
    ProductImage class
    """
    item = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL
    )
    title = models.CharField(
        max_length=254,
        null=True,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
