from django.contrib import admin

from .models import EntryData, DailyData
from users.models import CustomUser

# Register your models here.


admin.site.register([EntryData,DailyData,CustomUser])
