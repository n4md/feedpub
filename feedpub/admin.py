# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
##ADDED all below 12.5.18@5:18a
from .models import Feeditem, Feed

admin.site.register(Feeditem)
admin.site.register(Feed)
