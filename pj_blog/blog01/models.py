from __future__ import unicode_literals

from django.db import models


class Blog_News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null=True)

    def __unicode__(self):
        return self.title
