# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model 

from .models import Blog, book #, donor

User = get_user_model()
# Register your models here.
admin.site.register(Blog)
admin.site.register(book)
admin.site.register(User)