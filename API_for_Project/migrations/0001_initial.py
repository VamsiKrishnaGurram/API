# Generated by Django 5.0.1 on 2024-03-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poojas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pooja_id', models.CharField(max_length=10)),
                ('pooja_name', models.CharField(max_length=10)),
                ('Pooja_picture', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'poojas',
            },
        ),
    ]
