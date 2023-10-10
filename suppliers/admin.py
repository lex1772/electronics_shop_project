from django.contrib import admin
from django.utils.html import format_html

from config import settings
from contacts.models import Contact
from products.models import Product
from suppliers.models import Link


class ContactInLine(admin.StackedInline):
    model = Contact
    extra = 1


class ProductInLine(admin.StackedInline):
    model = Product
    extra = 1


@admin.action(description='Очистить задолженность перед поставщиком')
def cancel_the_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    inlines = [ContactInLine, ProductInLine, ]
    list_display = ('name', 'supplier', 'supplier_url', 'debt',
                    'creation_time', 'contacts',)
    list_filter = ('contact__city',)
    actions = (cancel_the_debt,)

    def supplier_url(self, obj):
        link_supplier = obj.supplier
        if link_supplier is not None:
            return format_html(
                f"<a href='{settings.BASE_URL}/admin/suppliers/link/"
                f"{link_supplier.id}'>{link_supplier.name}</a>")

    supplier_url.allow_tags = True
    supplier_url.short_description = 'Ссылка на поставщика'
