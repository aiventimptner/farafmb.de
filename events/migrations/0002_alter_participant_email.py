# Generated by Django 4.0.2 on 2022-03-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.CharField(max_length=200, verbose_name='Email'),
        ),
    ]
