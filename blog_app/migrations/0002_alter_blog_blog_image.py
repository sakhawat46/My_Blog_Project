# Generated by Django 3.2.9 on 2021-11-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Image'),
        ),
    ]
