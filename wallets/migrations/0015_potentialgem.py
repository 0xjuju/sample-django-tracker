# Generated by Django 4.1 on 2022-10-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0014_token_pair'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotentialGem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('ticker', models.CharField(default='', max_length=10)),
                ('contract_address', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
