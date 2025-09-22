from django.contrib import admin
from .models import Blog
@admin.register(Blog)
class admin(admin.ModelAdmin):
    ...

# Register your models here.
