from django.contrib import admin
from .models import vinyl_Order, OrderLineVinyl

# Models for editing through the Admin pannel 
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineVinyl


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(vinyl_Order, OrderAdmin)