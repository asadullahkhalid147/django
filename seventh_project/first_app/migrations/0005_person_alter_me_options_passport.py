# Generated by Django 5.0.1 on 2024-02-23 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_friend_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='me',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_number', models.IntegerField()),
                ('page', models.IntegerField()),
                ('validity', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first_app.person')),
            ],
        ),
    ]