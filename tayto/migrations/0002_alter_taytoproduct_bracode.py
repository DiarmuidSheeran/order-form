# Generated by Django 3.2.25 on 2024-06-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tayto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taytoproduct',
            name='bracode',
            field=models.IntegerField(blank=True, max_length=254, null=True),
        ),
    ]
