# Generated by Django 4.0.8 on 2022-10-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0017_targetwallet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetwallet',
            name='run_tracker',
            field=models.BooleanField(default=False),
        ),
    ]
