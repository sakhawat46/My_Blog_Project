# Generated by Django 3.2.9 on 2022-01-04 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blog_blog_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
    ]