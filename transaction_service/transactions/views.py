from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import TransactionForm, WalletForm
from .models import Transactions, Wallets


class CreateTransaction(CreateView):
    model = Transactions
    form_class = TransactionForm
    template_name = 'transactions/create_transaction.html'
    success_url = reverse_lazy('users:profile')

    def get_form_kwargs(self):
        kwargs = super(CreateTransaction, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def create_wallet(request):
    form = WalletForm(request.POST or None)
    if form.is_valid():
        wallet = form.save(commit=False)
        wallet.user = request.user
        wallet.save()
        return redirect('users:profile')
    return render(request, 'transactions/create_wallet.html',
                  {'form': form})
