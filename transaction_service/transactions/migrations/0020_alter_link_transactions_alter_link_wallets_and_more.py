# Generated by Django 4.0.3 on 2022-03-13 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0019_alter_wallets_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='transactions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transactions.transactions', verbose_name='Транзакции'),
        ),
        migrations.AlterField(
            model_name='link',
            name='wallets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transactions.wallets', verbose_name='Кошельки'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount_money',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма перевода'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction_recipient', to=settings.AUTH_USER_MODEL, verbose_name='Получатель'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction_sender', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='wallets_to_pay',
            field=models.ManyToManyField(through='transactions.Link', to='transactions.wallets', verbose_name='Кошельки для оплаты'),
        ),
        migrations.AlterField(
            model_name='wallets',
            name='money_rest',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Остаток средств'),
        ),
        migrations.AlterField(
            model_name='wallets',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя счёта'),
        ),
    ]