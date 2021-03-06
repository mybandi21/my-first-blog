# Generated by Django 3.2.2 on 2021-05-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('av_code', models.CharField(max_length=16)),
                ('av_title', models.CharField(blank=True, max_length=512)),
                ('av_contents', models.TextField(blank=True)),
                ('av_url', models.URLField(blank=True, null=True)),
                ('av_tag', models.TextField(blank=True)),
                ('cover_path', models.CharField(blank=True, max_length=512)),
                ('thum_path', models.CharField(blank=True, max_length=512)),
                ('actor_name', models.TextField(blank=True)),
                ('actor_code', models.CharField(blank=True, max_length=16)),
            ],
        ),
    ]
