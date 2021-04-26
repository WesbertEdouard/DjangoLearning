from django.contrib import admin

# Register your models here.
from .models import *

# Register Customer Model Table in Django Admin Portal
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
