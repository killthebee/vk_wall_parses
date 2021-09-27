from django.db import models


class ParseResults(models.Model):
    submission = models.CharField(max_length=250)
    image = models.ImageField(upload_to='wordclouds/')
    time = models.DateTimeField(auto_now=True)
    posts_data = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ('time', )
