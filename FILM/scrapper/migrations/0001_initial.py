# Generated by Django 3.0.8 on 2020-07-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('genre', models.CharField(max_length=40, verbose_name='Genre')),
                ('premier', models.DateField(verbose_name='Premier date')),
                ('avg_tomatometer', models.CharField(max_length=3, verbose_name='Tomato_Score')),
                ('avg_audience_score', models.CharField(max_length=3, verbose_name='Audience Score')),
            ],
        ),
    ]
