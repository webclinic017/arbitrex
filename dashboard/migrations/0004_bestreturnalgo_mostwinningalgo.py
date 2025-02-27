# Generated by Django 5.1.3 on 2024-11-26 04:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtesting', '0009_remove_backtestresult_end_date_and_more'),
        ('dashboard', '0003_bestperformingalgo_backtest_result'),
        ('strategies', '0003_remove_strategy_user_ratings_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestReturnAlgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algo_return', models.FloatField()),
                ('algo_win_rate', models.FloatField()),
                ('algo_sharpe_ratio', models.FloatField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('backtest_result', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_return_algos', to='backtesting.backtestresult')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='best_return_algos', to='strategies.strategy')),
            ],
        ),
        migrations.CreateModel(
            name='MostWinningAlgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algo_win_rate', models.FloatField()),
                ('algo_sharpe_ratio', models.FloatField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('backtest_result', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='most_winning_algos', to='backtesting.backtestresult')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='most_winning_algos', to='strategies.strategy')),
            ],
        ),
    ]
