# Generated by Django 3.0.6 on 2020-10-29 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20201029_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttype',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
    ]
