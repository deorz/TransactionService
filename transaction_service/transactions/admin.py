from django.contrib import admin

from .models import Transaction, Wallet, Link

admin.site.register(Transaction)
admin.site.register(Wallet)
admin.site.register(Link)
