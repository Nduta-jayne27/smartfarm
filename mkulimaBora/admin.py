from django.contrib import admin
from .models import *

# Register your models here.
class farmdataAdmin(admin.ModelAdmin):
	readonly_fields=('time',)
admin.site.register(farmdata,farmdataAdmin)
