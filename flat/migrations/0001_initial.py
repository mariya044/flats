# Generated by Django 2.1.5 on 2024-03-19 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('flor', models.PositiveIntegerField(blank=True, null=True)),
                ('all_floars', models.PositiveIntegerField(blank=True, null=True)),
                ('kitchen_square', models.PositiveIntegerField(blank=True, null=True)),
                ('all_square', models.PositiveIntegerField(blank=True, null=True)),
                ('living_square', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]