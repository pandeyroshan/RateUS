from django.contrib import admin
from .models import Department, Faculty, Rating, Subject,EntryCodes
# Register your models here.

admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Rating)
admin.site.register(Subject)
admin.site.register(EntryCodes)