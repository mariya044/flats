# Generated by Django 5.0.3 on 2024-03-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0007_post_all_square_post_flor_post_kitchen_square_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='all_floars',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
