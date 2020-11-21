# Sitemaps helps search engine indexers how frequently your pages change and
# how “important” certain pages are on our website.
#
# See:
#  https://docs.djangoproject.com/en/3.1/ref/contrib/sitemaps/

from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    # pylint: disable=no-self-use
    def lastmod(self, obj):
        return obj.updated
