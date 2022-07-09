# Generated by Django 4.0.5 on 2022-07-09 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(choices=[('MB', 'Mechanical Engineering'), ('VST', 'Process and Systems Engineering'), ('EIT', 'Electrical Engineering and Information Technology'), ('MA', 'Mathematics')], default='MB', max_length=3)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Study program',
                'verbose_name_plural': 'Study programs',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('phone', models.CharField(max_length=25, verbose_name='Mobile number')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mentoring.program')),
            ],
            options={
                'verbose_name': 'Mentor',
                'verbose_name_plural': 'Mentors',
            },
        ),
    ]
