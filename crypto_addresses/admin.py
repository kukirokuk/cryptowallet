from django.contrib import admin
from .models import Wallet, Address


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1

class WalletAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ('cryptocurrency',)

# admin.site.register(Address)
admin.site.register(Wallet, WalletAdmin)