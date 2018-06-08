# coding: utf-8

from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.files import get_thumbnailer


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    order = models.FloatField(default=0)
    publicated = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order']
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug or self.id})


class Post(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True)
    title = models.CharField(max_length=255)
    publicated = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(auto_now=True)
    viewed = models.IntegerField(default=0)
    content = RichTextUploadingField()
    preview_image = models.ImageField(upload_to='images/%Y/%m', verbose_name=u'Картинка превью')

    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = u'Запись'
        verbose_name_plural = u'Записи'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug or self.id})

    def get_preview_thumb(self, width=None, height=None):
        width = width if width else 295
        height = height if height else 132
        options = {'size': (width, height), 'crop': True}
        return get_thumbnailer(self.preview_image).get_thumbnail(options).url

    def increase_views_count(self):
        self.viewed = self.viewed + 1
        self.save()

    def get_excerpt(self):
        cnt = self.content.replace('page-break-after: always', 'page-break-after:always')
        return cnt.split('<div style="page-break-after:always"><span style="display:none">&nbsp;</span></div>', 1)[0]
