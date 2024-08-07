# Generated by Django 3.2.25 on 2024-07-02 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='walkersProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('productCode', models.CharField(blank=True, max_length=254, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('barcode', models.CharField(blank=True, max_length=254, null=True)),
                ('caseCount', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='walkers.category')),
            ],
            options={
                'verbose_name': 'Walkers Product',
                'verbose_name_plural': 'Walkers Products',
            },
        ),
    ]
