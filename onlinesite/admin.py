from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(logo)
@admin.register(group1)
class group1Admin(admin.ModelAdmin):
    list_display=('title','paragraph')

    
admin.site.register(group2)
admin.site.register(group3)
admin.site.register(group4)
admin.site.register(group5)
admin.site.register(group6)
admin.site.register(group7)
admin.site.register(group80)
admin.site.register(group81)
admin.site.register(group9)
admin.site.register(groups100)
admin.site.register(groups101)
admin.site.register(about1)
admin.site.register(about2)
admin.site.register(about3)
admin.site.register(about4_video)
admin.site.register(about6)
admin.site.register(service2)
admin.site.register(contact1)
admin.site.register(contact2)
admin.site.register(contact3)
admin.site.register(contact4)
admin.site.register(prices1)
admin.site.register(prices2)
admin.site.register(prices3)
admin.site.register(prices4)
admin.site.register(prices5)
admin.site.register(prices6)
