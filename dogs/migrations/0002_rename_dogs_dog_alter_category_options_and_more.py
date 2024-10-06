# Generated by Django 5.1.1 on 2024-09-26 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dogs',
            new_name='Dog',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='dog',
            options={'verbose_name': 'Dog', 'verbose_name_plural': 'Dogs'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='dog',
            table='Dogs',
        ),
    ]