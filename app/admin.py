from django.contrib import admin
from app import models

admin.site.register(models.DogProduct)
admin.site.register(models.Purchase)
admin.site.register(models.DogTag)