from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)  # iterable to order items by name
        verbose_name_plural = 'Categories' # to correct the spelling
    
    # to get the name u enter, instead of {category1, category2, ...}
    def __str__(self):
        return self.name

class Item(models.Model):
    # item + category's foreign key usage
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    # upload_to -> where on the server dy want this to be uploaded, a folder will be created by django
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # item + admin user -> gets item belonging to a particular user
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    keepactive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=100)
    price_range = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
class UserPreferences(models.Model):
    username = models.CharField(max_length=100)
    top_categories = models.CharField(max_length=255)  # Adjust field as per your data type needs

    def __str__(self):
        return f"User: {self.username}, Top Categories: {self.top_categories}"