# Generated by Django 2.2.9 on 2021-10-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20211022_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
