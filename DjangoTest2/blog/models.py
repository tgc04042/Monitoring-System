from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="image")
    photo = models.ImageField(upload_to="%Y/%m/%d")

class sensor(models.Model):
    s_name = models.CharField(max_length=20) # 1 : FC-28, 2 : GURTMGGG, 3 : 가내성

class humiditysensor(models.Model):
    s_type = models.AutoField(primary_key=True)
    s_date = models.DateTimeField(default=0)
    soil_humi = models.IntegerField(default=0)
    s_name = models.ForeignKey(sensor, on_delete=models.CASCADE)
    class Meta:
        ordering = ['s_type']

    def __str__(self):
        return[self.s_type, self.s_date, self.soil_humi, self.s_name]