from django.contrib import admin
from .models import Product, ProductImages, ShippingAddress, OrderItem, Order
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.db import models
from django.utils.translation import ugettext as _

# Register your models here.


class AdminImageWidget(AdminFileWidget):
    """
    Widget for Product Image in Product Detail Page
    """

    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s '
                % (image_url, image_url, file_name, _(""))
            )
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return format_html(u"".join(output))


class ProductImage(admin.TabularInline):
    """
    Inline Product Images
    """

    model = ProductImages
    formfield_overrides = {models.ImageField: {"widget": AdminImageWidget}}


class ProductAdmin(admin.ModelAdmin):

    """
    List Display Product Image

    """

    inlines = [ProductImage]

    formfield_overrides = {models.ImageField: {"widget": AdminImageWidget}}

    def image_tag(self, obj):
        try:
            return format_html('<img width=100 src="{}" />'.format(obj.image.url))
        except:
            return None

    list_display = ["image_tag", "title", "price"]

    readonly_fields = ["rating", "num_reviews"]


class ShippingAddressAdmin(admin.StackedInline):
    model = ShippingAddress
    # readonly_fields = ("address",)
    def has_change_permission(self, request, obj=None):
        return False

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fields = ("product", "qty", "price")
    def has_change_permission(self, request, obj=None):
        return False
    # readonly_fields = ("product",'qty','price')


class OrderAdmin(admin.ModelAdmin):
    inlines = [ShippingAddressAdmin, OrderItemAdmin]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [
                field.name
                for field in obj.__class__._meta.fields
                if field.name not in ["is_paid", "is_delivered"]
            ]
        return self.readonly_fields


admin.site.register(Order, OrderAdmin)

admin.site.register(Product, ProductAdmin)
