from django.db import models

# Category Models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    image = models.ImageField(upload_to='category_images/', null=True, blank=True, verbose_name='Image')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def image_url(self):
        return self.image.url if self.image else None

# Products models

class Product(models.Model):
    price_type_choices = (
        ('unitary', 'unit price'),
        ('closed package', 'Closed Package Price')
    )

    name = models.CharField(max_length=255, verbose_name='Name')
    image = models.ImageField(upload_to='products', default='image_default.png', verbose_name='image')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='get_products', verbose_name='Category')
    brand_name = models.CharField(max_length=255, verbose_name='Brand Name')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    price_type = models.CharField(max_length=100, choices=price_type_choices, default='unitary')
    stock = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    

class CarouselProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images')

    def __str__(self):
        return self.name