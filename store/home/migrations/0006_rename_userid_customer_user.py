# Generated by Django 4.1.3 on 2023-09-10 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_customer_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='userid',
            new_name='user',
        ),
    ]
