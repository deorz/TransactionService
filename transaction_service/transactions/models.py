import uuid

from django.db import models

from users.models import CustomUser


class Wallet(models.Model):
    user = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.CASCADE,
        related_name='wallets'
    )
    name = models.CharField(verbose_name='Имя счёта',
                            max_length=100, )
    money_rest = models.DecimalField(verbose_name='Остаток средств',
                                     max_digits=12,
                                     decimal_places=2,
                                     null=False)
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          unique=True,
                          editable=False,
                          )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'Имя счёта: {self.name}, остаток: {self.money_rest} у.е.'


class Transaction(models.Model):
    sender = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name='transaction_sender',
        verbose_name='Отправитель'
    )
    recipient = models.ForeignKey(
        CustomUser,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name='transaction_recipient',
        verbose_name='Получатель'
    )

    recipient_wallet = models.ForeignKey(
        Wallet,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name='recipient_wallet',
        verbose_name='Кошелёк получателя',
        help_text='Введите имя пользователя или почту получателя'
    )

    amount_money = models.DecimalField(verbose_name='Сумма перевода',
                                       max_digits=12,
                                       decimal_places=2,
                                       blank=False)

    wallets_to_pay = models.ManyToManyField(
        Wallet,
        through='Link',
        verbose_name='Кошельки для оплаты'
    )

    date_provided = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_provided']

    def __str__(self):
        return (f'{self.date_provided.strftime("%H:%M:%S %a %d-%m-%Y")} '
                f'перевод от {self.sender.get_full_name()} к '
                f'{self.recipient.get_full_name()} '
                f'сумма: {self.amount_money} у.е.')


class Link(models.Model):
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.DO_NOTHING,
        verbose_name='Кошелёк'
    )
    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        verbose_name='Транзакция'
    )

    def __str__(self):
        return (f'{self.transaction.id}: {self.transaction.sender} - '
                f'{self.transaction.recipient}')
