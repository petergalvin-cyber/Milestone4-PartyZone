from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem
    extra = 1 

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)

# Register your models here.
