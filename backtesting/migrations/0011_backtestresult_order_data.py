# Generated by Django 5.1.3 on 2024-11-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtesting', '0010_backtestresult_portfolio_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='backtestresult',
            name='order_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
