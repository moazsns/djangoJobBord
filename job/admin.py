from django.contrib import admin

# Register your models here.

from .models import Job , Ctegory

admin.site.register(Job)

admin.site.register(Ctegory)