from django.contrib import admin
from applications.product.models import *

admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Rating)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]


admin.site.register(Product, ProductAdmin)
