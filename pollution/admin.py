from django.contrib import admin
from .models import PollutionData, Vehicle, City

# Register your models here.
admin.site.register(PollutionData)
admin.site.register(Vehicle)
admin.site.register(City)