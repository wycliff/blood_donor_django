# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Blog, book, donor


# Register your models here.
admin.site.register(Blog)
admin.site.register(book)
admin.site.register(donor)