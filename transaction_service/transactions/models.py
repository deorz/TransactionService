import uuid

from django.db import models

from users.models import CustomUser


class Wallets(models.Model):
    user = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.CASCADE,
        related_name='wallets'
    )
    name = models.CharField(max_length=100, default='')
    money_rest = models.DecimalField(max_digits=19,
                                     decimal_places=10,
                                     null=False)
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          unique=True,
                          editable=False,
                          )

    def __str__(self):
        return f'Счёт: {self.name}, остаток: {self.money_rest}'


class Transactions(models.Model):
    sender = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name='transactions',
    )
    recipient = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name='transactions_recipient'
    )
    amount_money = models.DecimalField(max_digits=19,
                                       decimal_places=10,
                                       blank=False)
    wallets_to_pay = models.ForeignKey(
        Wallets,
        on_delete=models.DO_NOTHING
    )
    date = models.DateTimeField(auto_now_add=True)
