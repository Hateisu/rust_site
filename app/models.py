from django.db import models

# Create your models here.

class RustVideo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', unique=True)
    image = models.ImageField(upload_to='rust_preview', verbose_name='Preview', blank=False)
    description = models.CharField(max_length=150, verbose_name='Описание', unique=True)
    video_src = models.FileField(upload_to='rust_video', verbose_name='Видео', blank=True)
    video_url = models.CharField(max_length=400, verbose_name='URL', unique=True)


class DotaVideo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', unique=False)
    image = models.ImageField(upload_to='dota_preview', verbose_name='Preview', blank=False)
    description = models.CharField(max_length=150, verbose_name='Описание', unique=False)
    video_src = models.FileField(upload_to='dota_video', verbose_name='Видео', blank=True)
    video_url = models.CharField(max_length=400, verbose_name='URL', unique=False)