# Generated by Django 4.2 on 2023-04-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
