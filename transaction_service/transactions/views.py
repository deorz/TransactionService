from dal import autocomplete
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, DetailView

from .forms import TransactionForm, WalletForm
from .models import Transaction, Link, Wallet


class WalletsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Wallet.objects.none()
        queryset = Wallet.objects.all().exclude(user=self.request.user)
        if self.q:
            queryset = queryset.filter(
                Q(user__username__contains=self.q) |
                Q(user__email__contains=self.q)
            )
        return queryset


class CreateTransactionView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/create_transaction.html'
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.sender = self.request.user
        transaction.recipient = transaction.recipient_wallet.user
        super().form_valid(form)
        self.send_money(transaction)
        return super().form_valid(form)

    def send_money(self, transaction):
        links = Link.objects.filter(transactions_id=transaction.id)
        recipient_wallet_id = transaction.recipient_wallet.id
        money_to_send = transaction.amount_money
        money_to_send_divided = money_to_send / len(links)
        for link in links:
            wallet = Wallet.objects.get(id=link.wallets_id)
            wallet.money_rest -= money_to_send_divided
            if wallet.money_rest < 0:
                transaction.delete()
                raise ValidationError(_(
                    'На одном или нескольких счетах недостаточно денег'
                ))
            wallet.save()
        recipient_wallet = Wallet.objects.get(id=recipient_wallet_id)
        recipient_wallet.money_rest += money_to_send
        recipient_wallet.save()
        return

    def get_form_kwargs(self):
        kwargs = super(CreateTransactionView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class CreateWalletView(LoginRequiredMixin, CreateView):
    model = Wallet
    form_class = WalletForm
    template_name = 'transactions/create_wallet.html'
    success_url = reverse_lazy('users:profile')

    def get_form_kwargs(self):
        kwargs = super(CreateWalletView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        wallet = form.save(commit=False)
        wallet.user = self.request.user
        wallet.save()
        return super().form_valid(form)


class WalletListView(LoginRequiredMixin, ListView):
    template_name = 'transactions/wallet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)


class TransactionHistoryView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = 'transactions/transaction_history.html'

    def get_queryset(self):
        base_queryset = Transaction.objects.filter(
            Q(sender=self.request.user) |
            Q(recipient=self.request.user))
        if self.kwargs.get('name') is not None:
            base_queryset = base_queryset.filter(
                Q(recipient_wallet__name=self.kwargs['name']) |
                Q(wallets_to_pay__name=self.kwargs['name']))
        if self.kwargs.get('order_by') is not None:
            base_queryset = base_queryset.order_by(
                self.kwargs.get('order_by'))
        return base_queryset

    def get_context_data(self, **kwargs):
        context = super(TransactionHistoryView,
                        self).get_context_data(**kwargs)
        wallets = Wallet.objects.filter(user=self.request.user)
        order_by = self.kwargs.get('order_by')
        sort_by = self.kwargs.get('name')
        context['wallets'] = wallets
        context['order_by'] = order_by
        context['sort_by'] = sort_by
        return context


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'transactions/transaction_detail.html'


class WalletDetailView(LoginRequiredMixin, DetailView):
    model = Wallet
    template_name = 'transactions/wallet_detail.html'
