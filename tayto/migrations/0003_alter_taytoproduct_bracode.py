# Generated by Django 3.2.25 on 2024-06-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tayto', '0002_alter_taytoproduct_bracode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taytoproduct',
            name='bracode',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
