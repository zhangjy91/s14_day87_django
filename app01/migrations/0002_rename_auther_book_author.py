# Generated by Django 3.2.12 on 2022-03-25 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='auther',
            new_name='author',
        ),
    ]
