# Generated by Django 5.0.6 on 2024-05-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
