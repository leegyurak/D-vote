# Generated by Django 3.1.1 on 2020-09-09 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=60)),
                ('item1', models.CharField(max_length=20)),
                ('item2', models.CharField(max_length=20)),
                ('item3', models.CharField(max_length=20, null=True)),
                ('item4', models.CharField(max_length=20, null=True)),
                ('item5', models.CharField(max_length=20, null=True)),
                ('item1Cnt', models.IntegerField(default=0)),
                ('item2Cnt', models.IntegerField(default=0)),
                ('item3Cnt', models.IntegerField(null=True)),
                ('item4Cnt', models.IntegerField(null=True)),
                ('item5Cnt', models.IntegerField(null=True)),
                ('is_consent', models.BooleanField(default=False)),
                ('select', models.CharField(choices=[('accept', 'accept'), ('deny', 'deny')], max_length=7)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
