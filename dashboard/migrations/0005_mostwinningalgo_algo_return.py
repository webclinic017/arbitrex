# Generated by Django 5.1.3 on 2024-11-26 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_bestreturnalgo_mostwinningalgo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mostwinningalgo',
            name='algo_return',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]