from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from transactions.models import Wallets
from .forms import UserRegisterForm


class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/sign_up.html'


def profile(request):
    user = request.user
    wallets_money = Wallets.objects.filter(user=user).values(
        'money_rest')
    money_rest = 0
    for money in wallets_money:
        money_rest += money['money_rest']
    context = {
        'money_rest': money_rest
    }
    return render(request, 'users/profile.html', context=context)
