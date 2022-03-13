from django import forms
from django.core.exceptions import ValidationError

from users.models import CustomUser
from .models import Wallets, Transactions


class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['recipient'].empty_label = 'Пользователь не выбран'
        self.fields['wallets_to_pay'].queryset = Wallets.objects.filter(
            user=self.request.user
        )
        self.fields[
            'recipient'].queryset = CustomUser.objects.all().exclude(
            username=self.request.user
        )

    wallets_to_pay = forms.ModelMultipleChoiceField(
        queryset=None, widget=forms.CheckboxSelectMultiple
    )

    recipient = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = Transactions
        fields = ('recipient', 'amount_money', 'wallets_to_pay')


class WalletForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Wallets
        fields = ('name', 'money_rest')

    def clean_money_rest(self):
        money_rest = self.cleaned_data['money_rest']
        if money_rest == 0:
            raise ValidationError('На вашем кошельке не может быть 0')
        return money_rest

    def clean_name(self):
        name = self.cleaned_data['name']
        user = self.request.user
        names_queryset = Wallets.objects.filter(
            user=user).values('name')
        for names in names_queryset:
            if name == names['name']:
                raise ValidationError(
                    'У вас уже есть кошелёк с таким именем'
                )
        return name
