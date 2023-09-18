from django.contrib import admin

# Register your models here.
from home.models import contact,Product,Order,Customer
admin.site.register(contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
