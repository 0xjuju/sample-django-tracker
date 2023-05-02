# Generated by Django 4.1 on 2022-10-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0015_potentialgem'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=255)),
                ('contract', models.CharField(default='', max_length=255)),
                ('abi', models.TextField(default='')),
                ('balance', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
