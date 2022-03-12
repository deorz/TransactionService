from django.contrib import admin

from .models import Transactions, Wallets

admin.site.register(Transactions)
admin.site.register(Wallets)
