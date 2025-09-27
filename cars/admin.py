from django.contrib import admin
from cars.models import Brand, Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)
    list_filter = ('factory_year', 'model_year')

admin.site.register(Car, CarAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)    
