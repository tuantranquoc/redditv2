# Generated by Django 3.0.6 on 2020-10-21 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_auto_20201021_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['id']},
        ),
    ]
