from django.db import models


class Data(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.URLField(max_length=250)
    url = models.URLField(max_length=250)

    def __str__(self):
        return self.title
