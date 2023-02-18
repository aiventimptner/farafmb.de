# Generated by Django 4.1.6 on 2023-02-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('link', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
