# Generated by Django 4.2.9 on 2024-05-13 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_commande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='total',
        ),
    ]
