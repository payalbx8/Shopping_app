from django.contrib import admin
from ecommerceapp.models import contact,Product,Orders,OrderUpdate
# Register your models here.
admin.site.register(contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)