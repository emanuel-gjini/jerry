# Generated by Django 3.1.5 on 2021-01-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.TextField(null=True),
        ),
    ]