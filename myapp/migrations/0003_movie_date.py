# Generated by Django 5.0.6 on 2024-06-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_user_name_movie_person_name_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
