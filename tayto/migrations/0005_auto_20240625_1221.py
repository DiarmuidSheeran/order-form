# Generated by Django 3.2.25 on 2024-06-25 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tayto', '0004_alter_taytoproduct_productcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taytoproduct',
            options={'verbose_name': 'Tayto Product', 'verbose_name_plural': 'Tayto Products'},
        ),
        migrations.RenameField(
            model_name='taytoproduct',
            old_name='bracode',
            new_name='barcode',
        ),
    ]
