from django.db import models

# Create your models here.


class CodingPics(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='cool_coding_images')

    class Meta: 
        verbose_name_plural = 'Coding Pics'

    def __str__(self):
        return self.name