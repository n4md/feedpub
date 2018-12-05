# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid ##ADDED 12.5.18@5:20a
import datetime ##ADDED 12.5.18@5:20a

# Create your models here.
##ADDED all below 12.5.18@5:20a
class Feed(models.Model):
    feedName = models.CharField(max_length=200)
    lastUpdate = models.DateTimeField('date of last update')
    def __str__(self):
        return self.feedName

class Feeditem(models.Model):
    uid = models.CharField(max_length=40, default=uuid.uuid4)
    updateDate = models.DateTimeField('date of item creation', default=datetime.datetime.now)
    titleText = models.CharField(max_length=200)
    streamUrl = models.CharField(max_length=200, blank=True)
    contentText = models.TextField()
    redirectionUrl = models.CharField(max_length=200)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    def __str__(self):
        return self.titleText
