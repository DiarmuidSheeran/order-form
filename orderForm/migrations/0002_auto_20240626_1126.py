# Generated by Django 3.2.25 on 2024-06-26 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tayto', '0005_auto_20240625_1221'),
        ('orderForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderForm.taytoorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tayto.taytoproduct')),
            ],
        ),
        migrations.AddField(
            model_name='taytoorder',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='orderForm.OrderProduct', to='tayto.taytoProduct'),
        ),
    ]
