# Generated by Django 4.0.3 on 2022-03-15 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0023_rename_transactions_transaction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='recipient_wallet',
            field=models.ForeignKey(default='26bdd13d-8113-4147-b798-30fa5f7aa1c6', on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipient_wallet', to='transactions.wallet', verbose_name='Кошелёк получателя'),
            preserve_default=False,
        ),
    ]
