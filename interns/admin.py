from django.contrib import admin

# Register your models here.
from .models import transporter
from .models import distrubuter

admin.site.register(transporter)
admin.site.register(distrubuter)
