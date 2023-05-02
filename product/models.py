from io import BytesIO
from os import name
from PIL import Image
from django.core.files import File
from accounts.models import CustomUser
from django.db import models
from accounts.models import SellerProfile

 #convert image
def convert_image_to_rgb(image):
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        rgb_image = Image.new("RGB", image.size, (255, 255, 255))
        rgb_image.paste(image, mask=image.split()[3])  # 3 is the alpha channel
        return rgb_image
    else:
        return image
    
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Product(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey(SellerProfile, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True) # Change uploads to thumbnails 
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail2 = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail3 = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail4 = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)

    def get_average_rating(self):
        average = self.ratings.aggregate(average=models.Avg('rating'))['average']
        if average:
            return round(average, 1)
        return 0

    class Meta:
        ordering = ['-added_date']

    def __str__(self):
        return self.title

    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            
            else:
                # Default Image
                return 'https://via.placeholder.com/240x180.jpg'
    
   
    # Generating Thumbnail - Thumbnail is created when get_thumbnail is called
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img2 = convert_image_to_rgb(img)
        #img.convert('RGB')
       
        img2.thumbnail(size)

        thumb_io = BytesIO()
        img2.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class ProductReport(models.Model):
    
    listing = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.pk} - {self.listing}"
    
class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Ratings range from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Each user can rate a product only once