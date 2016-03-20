# coding: utf-8

from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    title = models.CharField(max_length=255)
    publicated = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()

    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug or self.id})

    def get_excerpt(self):
        return self.content.split('<div style="page-break-after: always"><span style="display:none">&nbsp;</span></div>', 1)[0]

