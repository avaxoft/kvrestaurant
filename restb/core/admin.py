from django.contrib import admin
from . import models
# Register your models here.



admin.site.register(models.Item)
admin.site.register(models.Deal)
admin.site.register(models.DealItem)
admin.site.register(models.Order)