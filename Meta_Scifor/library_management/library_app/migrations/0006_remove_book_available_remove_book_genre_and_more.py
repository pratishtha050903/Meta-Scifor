# Generated by Django 5.1.5 on 2025-03-06 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_remove_borrow_return_date_borrow_returned_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='available',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_year',
        ),
    ]
