# Generated by Django 5.0.6 on 2024-06-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_rename_cat_women_cat_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='cat_id',
            new_name='cat',
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
