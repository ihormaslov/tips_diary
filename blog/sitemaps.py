from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.filter(publicated=True)

    def lastmod(self, obj):
        return obj.modified


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Category.objects.filter(publicated=True)

    def lastmod(self, obj):
        return obj.modified
