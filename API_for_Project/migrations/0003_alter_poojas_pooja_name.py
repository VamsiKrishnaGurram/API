# Generated by Django 5.0.1 on 2024-03-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_for_Project', '0002_alter_poojas_pooja_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poojas',
            name='pooja_name',
            field=models.CharField(max_length=50),
        ),
    ]
