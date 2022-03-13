from django.urls import path

from . import views

app_name = 'transactions'

urlpatterns = [
    path('create_transaction/', views.CreateTransaction.as_view(),
         name='create_transaction'
         ),
    path('create_wallet/', views.create_wallet, name='create_wallet')
]
