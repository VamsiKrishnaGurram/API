# Generated by Django 4.2.11 on 2024-04-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_for_Project', '0006_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poojas',
            name='Pooja_picture',
            field=models.ImageField(null=True, upload_to='static/Pooja_picture'),
        ),
    ]