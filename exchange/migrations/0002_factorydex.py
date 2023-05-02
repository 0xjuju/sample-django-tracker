# Generated by Django 4.0.8 on 2022-10-23 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactoryDex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('abi', models.TextField()),
                ('version', models.IntegerField(default=0)),
            ],
        ),
    ]