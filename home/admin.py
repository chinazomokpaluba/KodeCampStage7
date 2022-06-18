from django.contrib import admin
from .models import People,Doctor,Bio,Address,Product

admin.site.register(People)
admin.site.register(Doctor)
admin.site.register(Bio)
admin.site.register(Address)
admin.site.register(Product)
# Register your models here.
