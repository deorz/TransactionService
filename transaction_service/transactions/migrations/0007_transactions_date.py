# Generated by Django 4.0.3 on 2022-03-13 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_wallets_name_alter_transactions_recipient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
