from django.contrib import admin

# Register your models here.
from .models import Grade, Week
admin.site.register(Grade)
admin.site.register(Week)