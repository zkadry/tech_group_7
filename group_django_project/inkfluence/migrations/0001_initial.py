# Generated by Django 5.0.2 on 2024-02-28 16:57

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='group_django_project/files/profile_pics')),
                ('bio', models.TextField(max_length=300)),
                ('genre_likes', multiselectfield.db.fields.MultiSelectField(choices=[('FAN', 'Fantasy'), ('SCF', 'Sci-Fi'), ('ACT', 'Action & Adventure'), ('MYS', 'Mystery'), ('HOR', 'Horror'), ('THR', 'Thriller & Crime'), ('HIS', 'Historical Fiction'), ('ROM', 'Romance'), ('COM', 'Comedy'), ('YA', 'Young Adult'), ('CHI', 'Children')], max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('FAN', 'Fantasy'), ('SCF', 'Sci-Fi'), ('ACT', 'Action & Adventure'), ('MYS', 'Mystery'), ('HOR', 'Horror'), ('THR', 'Thriller & Crime'), ('HIS', 'Historical Fiction'), ('ROM', 'Romance'), ('COM', 'Comedy'), ('YA', 'Young Adult'), ('CHI', 'Children')], max_length=200)),
                ('description', models.TextField(max_length=300)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='inkfluence.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('body', models.CharField(max_length=500)),
                ('rating', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='inkfluence.story')),
            ],
        ),
    ]
