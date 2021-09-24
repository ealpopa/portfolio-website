from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
