from django.db import models

# Create your models here.

class Article(models.Model):
    av_code = models.CharField(max_length = 16)
    av_title = models.CharField(max_length = 512, blank=True)
    av_contents = models.TextField(blank=True)
    av_url = models.URLField(blank=True, null=True)
    av_tag = models.TextField(blank=True)
    cover_path = models.CharField(max_length = 512, blank=True)
    thum_path = models.CharField(max_length = 512, blank=True)
    actor_name = models.TextField(blank=True)
    actor_code = models.CharField(max_length = 16, blank=True)
