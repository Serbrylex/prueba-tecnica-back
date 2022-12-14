# Generated by Django 4.1.2 on 2022-10-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('price_without_tax', models.IntegerField()),
                ('shipping_fee', models.IntegerField()),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
