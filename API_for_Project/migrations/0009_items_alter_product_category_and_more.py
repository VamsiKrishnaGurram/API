# Generated by Django 4.2.11 on 2024-04-08 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_for_Project', '0008_alter_poojas_pooja_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_list', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('OP', 'Occasional'), ('FP', 'Festival'), ('HP', 'Homas')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='API_for_Project/static/Pooja_picture'),
        ),
        migrations.AddField(
            model_name='product',
            name='Items',
            field=models.ManyToManyField(to='API_for_Project.items'),
        ),
    ]
