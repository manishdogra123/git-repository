from django.contrib import admin
from .models import product
from .models import category
from .models import customer

# Register your models here.
class Adminproduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class Admincategory(admin.ModelAdmin):
    list_display = ['name']

class Admincustomer(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'email', 'phone']
admin.site.register(product,Adminproduct)
admin.site.register(category,Admincategory)
admin.site.register(customer,Admincustomer)
# admin.site.register(category)
 