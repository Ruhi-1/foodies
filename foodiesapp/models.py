from django.db import models





# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     # image = models.SlugField(upload_to='products/YY/MM/DD', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

# class Meta:
#     ordering = ('-created',)
#     index_together = (('id', 'slug'),)

# def __str__(self):
#     return self.name