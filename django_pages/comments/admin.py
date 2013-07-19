# -*- encoding: utf-8 -*-

from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', '__unicode__', 'user', 'post', 'ip')
    list_display_links = ('id', '__unicode__')
