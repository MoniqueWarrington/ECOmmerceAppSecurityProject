# Generated by Django 2.2 on 2019-05-02 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190502_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
