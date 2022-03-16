from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from transactions.models import Wallet, Transaction
from .forms import UserRegisterForm


class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/sign_up.html'


class Profile(LoginRequiredMixin, ListView):
    template_name = 'users/profile.html'

    def get_queryset(self):
        return Transaction.objects.filter(
            Q(sender=self.request.user) |
            Q(recipient=self.request.user)
        )[:5]

    def get_context_data(self, **kwargs):
        kwargs.setdefault('money_rest', self.get_money_rest)
        return super().get_context_data(**kwargs)

    def get_money_rest(self):
        user = self.request.user
        wallets = Wallet.objects.filter(user=user)
        money_rest = 0
        for wallet in wallets:
            money_rest += wallet.money_rest
        return money_rest
