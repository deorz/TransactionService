# Generated by Django 4.0.3 on 2022-03-13 15:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_rename_date_transactions_date_provided'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='wallets_to_pay_new',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.DO_NOTHING, related_name='wallets', to='transactions.wallets'),
        ),
    ]
