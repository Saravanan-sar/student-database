# Generated by Django 5.2 on 2025-06-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
