# Generated by Django 5.0.3 on 2024-03-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
