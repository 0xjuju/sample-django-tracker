# Generated by Django 4.1 on 2022-09-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0004_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='chain',
            field=models.CharField(default='', max_length=255),
        ),
    ]