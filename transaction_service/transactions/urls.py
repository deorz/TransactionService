from django.urls import path
from django.urls import re_path as url

from . import views

from .models import Wallet

app_name = 'transactions'

urlpatterns = [
    path('create_transaction/', views.CreateTransactionView.as_view(),
         name='create_transaction'),
    path('create_wallet/', views.CreateWalletView.as_view(),
         name='create_wallet'),
    path('wallet_list/', views.WalletListView.as_view(),
         name='wallet_list'),
    path('transaction_history/', views.TransactionHistoryView.as_view(),
         name='transaction_history'),
    path('transaction/<int:pk>/', views.TransactionDetailView.as_view(),
         name='transaction_detail'),
    path('wallet/<uuid:pk>/', views.WalletDetailView.as_view(),
         name='wallet_detail'),
    url('wallet-autocomplete/',
        views.WalletsAutocomplete.as_view(),
        name='wallet-autocomplete'),
]
