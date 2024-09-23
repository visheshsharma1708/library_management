# Generated by Django 5.0.7 on 2024-09-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_library_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='roll_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]