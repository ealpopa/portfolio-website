from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def get_preview(self):
        return self.body[:20] + ' [...]'

    def __str__(self):
        return self.title