# Generated by Django 3.0.7 on 2020-06-16 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0002_auto_20200616_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('GR', 'Greek'), ('EN', 'English'), ('DE', 'German'), ('SP', 'Spanish'), ('IT', 'Italian'), ('RS', 'Russian'), ('CH', 'Chinese')], default='GR', max_length=2)),
                ('currency', models.CharField(choices=[('EUR', 'Euro'), ('USD', 'US Dollar'), ('GBP', 'UK Pound')], default='EUR', max_length=3)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Shop')),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.Menu')),
                ('menu_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.MenuCategory')),
            ],
        ),
    ]
