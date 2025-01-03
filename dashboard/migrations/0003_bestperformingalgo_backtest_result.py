# Generated by Django 5.1.3 on 2024-11-23 04:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backtesting", "0002_backtestresult_algo_return_and_more"),
        ("dashboard", "0002_bestperformingalgo_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="bestperformingalgo",
            name="backtest_result",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="best_performances",
                to="backtesting.backtestresult",
            ),
        ),
    ]
