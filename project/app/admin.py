from django.contrib import admin
from .models import Member, City, Country

# Register your models here.

admin.site.register(Member)
admin.site.register(City)
admin.site.register(Country)