from django.contrib import admin
from django.utils.safestring import mark_safe

from drugs.models import Category, AgroProductImage, AgroProduct


class ProductImageInline(admin.TabularInline):
    model = AgroProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name", "desc"
    list_filter = "name",


@admin.register(AgroProduct)
class AgroProductAdmin(admin.ModelAdmin):
    list_display = "name", 'status', "desc", "price", "category__name", "display_images"
    list_filter = "name", "price"
    inlines = [ProductImageInline]

    def display_images(self, obj):
        images = obj.images.all()
        if images.exists():
            return mark_safe(f"<img src='{images[0].image.url}' width='100px' height='100px' />")
        return "No image"

    display_images.short_description = "Preview"


@admin.register(AgroProductImage)
class AgroProductImageAdmin(admin.ModelAdmin):
    list_display = "product_images", "product__name"
    list_filter = "product__name",


    def product_images(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='100px' height='100px' />")
        return "No image"

    product_images.short_description = "Images"
