# Generated by Django 3.0.7 on 2020-11-23 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0029_auto_20201122_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackListType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='VIEW_ONLY', max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
                ('from_timestamp', models.DateTimeField(auto_now_add=True)),
                ('to_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityBlackListDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blacklist_type', models.ManyToManyField(blank=True, to='community.BlackListType')),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityBlackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blacklist_detail', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.CommunityBlackListDetail')),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Community')),
            ],
        ),
    ]
