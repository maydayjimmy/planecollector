from django.contrib import admin
# import your models here
from .models import Flight, History

# Register your models here
admin.site.register(Flight)
admin.site.register(History)
