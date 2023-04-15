from django.db import models
import os
import datetime

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join("uploads/", filename)
# Create your models here.

 #job = models.ForeignKey(User, related_name='add_jobs', on_delete=models.CASCADE)
class Category(models.Model): 
    slug = models.CharField(max_length=60, null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    image = models.ImageField(upload_to='image_upload', null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    meta_title = models.CharField(max_length=60, null=False, blank=False )
    meta_keywords = models.CharField(max_length=60, null=False, blank=False)
    meta_description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
  

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=60, null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    product_image = models.ImageField(upload_to='image_upload', null=False, blank=False)
    small_description = models.CharField(max_length=60, null=False, blank=False)
    quantity = models.IntegerField(default=1)
    description = models.TextField(max_length=1000, null=False, blank=False)
    original_price = models.IntegerField(default=1)
    selling_price = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    trending = models.BooleanField(default=True)
    tag = models.CharField(max_length=60, null=False, blank=False)
    meta_title = models.CharField(max_length=60, null=False, blank=False )
    meta_keywords = models.CharField(max_length=60, null=False, blank=False)
    meta_description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    