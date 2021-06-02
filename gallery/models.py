from django.db import models

# Create your models here.


class Gallery(models.Model):
    description  = models.CharField(default='内容', max_length=500)
    image= models.ImageField(default='default.png',upload_to='images/')

    title = models.CharField(default='作品标题', max_length=100)
    def __str__(self):
        return self.title
        




