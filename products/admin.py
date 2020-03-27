from django.contrib import admin
from .models import Product, Theme

"""
class ProductAdminInLine(admin.TabularInline):
    model = Product

class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductAdminInLine,)
"""

admin.site.register(Product)
admin.site.register(Theme)
# Register your models here.

