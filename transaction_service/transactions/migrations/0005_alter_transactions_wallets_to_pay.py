# Generated by Django 4.0.3 on 2022-03-12 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_rename_uuid_wallets_id_remove_wallets_wallet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='wallets_to_pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transactions.wallets'),
        ),
    ]