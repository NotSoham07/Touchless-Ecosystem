from django.contrib import admin

# Register your models here.
from .models import Feedback, Product, Joinus, Orders

admin.site.register(Feedback)
admin.site.register(Product)
admin.site.register(Joinus)
admin.site.register(Orders)