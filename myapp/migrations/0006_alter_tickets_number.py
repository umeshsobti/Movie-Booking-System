# Generated by Django 5.0.6 on 2024-06-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_tickets_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='number',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
