# Generated by Django 2.1.5 on 2024-03-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0002_auto_20240324_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='adress',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
