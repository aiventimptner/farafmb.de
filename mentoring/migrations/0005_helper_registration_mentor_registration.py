# Generated by Django 4.0.6 on 2022-07-16 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0004_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='registration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mentoring.registration', verbose_name='Registration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='registration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mentoring.registration', verbose_name='Registration'),
            preserve_default=False,
        ),
    ]
