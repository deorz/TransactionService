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
    money_rest = models.PositiveBigIntegerField(null=False)
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          unique=True,
                          editable=False,
                          )


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
    amount_money = models.PositiveBigIntegerField(blank=False)
    wallets_to_pay = models.ForeignKey(
        Wallets,
        on_delete=models.DO_NOTHING
    )
