# Generated by Django 4.2.1 on 2023-06-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_variation_price_alter_variation_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occassion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual', models.CharField(default='Casuals', max_length=50)),
                ('Formal', models.CharField(default='Formals', max_length=50)),
                ('Sports', models.CharField(default='Sports', max_length=50)),
            ],
        ),
    ]
