# Generated by Django 4.0.3 on 2022-03-12 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_remove_wallets_id_alter_wallets_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallets',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='wallets',
            name='wallet_id',
        ),
    ]