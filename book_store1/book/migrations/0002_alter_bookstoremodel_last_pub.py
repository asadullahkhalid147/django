# Generated by Django 5.0.1 on 2024-02-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoremodel',
            name='last_pub',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
