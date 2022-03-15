from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser
from .models import Wallet, Transaction

from dal import autocomplete


class TransactionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')

        super().__init__(*args, **kwargs)

        self.fields[
            'wallets_to_pay'] = forms.ModelMultipleChoiceField(
            queryset=Wallet.objects.filter(
                user=self.request.user),
            widget=forms.CheckboxSelectMultiple,
            label='Кошельки для оплаты')

        # self.fields['recipient'] = forms.ModelChoiceField(
        #     queryset=CustomUser.objects.all().exclude(
        #         username=self.request.user),
        #     label='Получатель')

        # self.fields[
        #     'recipient_wallet'].queryset = Wallet.objects.all().exclude(
        #     user=self.request.user)

        # self.fields[
        #     'recipient'].empty_label = 'Пользователь не выбран'

    class Meta:
        model = Transaction
        fields = ('recipient_wallet',
                  'wallets_to_pay',
                  'amount_money')
        widgets = {
            'recipient_wallet': autocomplete.ModelSelect2(
                url='wallet-autocomplete/')
        }

    def clean_amount_money(self):
        amount_money = self.cleaned_data['amount_money']
        if amount_money <= 0:
            raise ValidationError(
                _('Вы не можете перевести эту сумму'))
        return amount_money


class WalletForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Wallet
        fields = ('name',
                  'money_rest')

    def clean_money_rest(self):
        money_rest = self.cleaned_data['money_rest']
        if money_rest < 0:
            raise ValidationError(_(
                'На вашем кошельке не может быть отрицательная сумма'
            ))
        return money_rest

    def clean_name(self):
        name = self.cleaned_data['name']
        user = self.request.user
        names_queryset = Wallet.objects.filter(
            user=user).values('name')
        for names in names_queryset:
            if name == names['name']:
                raise ValidationError(_(
                    'У вас уже есть кошелёк с таким именем'
                ))
        return name
