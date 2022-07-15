from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TheUser, Item

admin.site.register(TheUser, UserAdmin)
admin.site.register(Item)

