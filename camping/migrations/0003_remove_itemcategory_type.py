# Generated by Django 4.2.6 on 2023-10-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0002_item_slug_itemcategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcategory',
            name='type',
        ),
    ]