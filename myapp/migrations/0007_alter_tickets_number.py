# Generated by Django 5.0.6 on 2024-06-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_tickets_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
