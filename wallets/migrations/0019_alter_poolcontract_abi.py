# Generated by Django 4.0.8 on 2022-10-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0018_targetwallet_run_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolcontract',
            name='abi',
            field=models.TextField(default=''),
        ),
    ]