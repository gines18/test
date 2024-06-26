# Generated by Django 5.0.3 on 2024-03-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_customer_remove_menu_category_id_delete_menuitems_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('time_log', models.TimeField()),
                ('reservation_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
