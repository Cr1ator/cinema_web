from email.mime import image
from django.db import models
 

class Setting(models.Model):
    title = models.CharField(max_length=250)
    decription = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    tel = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    google = models.CharField(max_length=255)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class About(models.Model):
    description = models.TextField()
    image_about = models.ImageField(upload_to = "about/")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"