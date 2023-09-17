from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime
from .utils import img_compress


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Category, self).save(*args, **kwargs)
    

class Listing(models.Model):
    category = models.ForeignKey(Category, related_name='listings', on_delete=models.CASCADE)
    created_by = models.ForeignKey(get_user_model(), related_name='listings', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.TextField()
    amount = models.IntegerField(default=10000, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)
    is_sold = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name} - {self.category} - {self.created_by}"
    
    def get_absolute_url(self):
        return reverse("list_detail", args=[self.slug])
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return 'https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + '-' + self.created_by.email + '-' + self.location + '-' + str(datetime.now()))

        if self.image:
            self.thumbnail = img_compress(self.image)
            
        return super(Listing, self).save(*args, **kwargs)
