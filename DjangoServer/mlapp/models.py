from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='userUploaded/%Y_%m_%d/', blank=True)
    
    def __str__(self):
        return self.title