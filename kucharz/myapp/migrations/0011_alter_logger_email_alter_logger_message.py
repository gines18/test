# Generated by Django 5.0.3 on 2024-03-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_logger_time_log_logger_email_logger_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='logger',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
