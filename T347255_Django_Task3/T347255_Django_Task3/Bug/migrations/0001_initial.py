# Generated by Django 4.2.5 on 2023-10-05 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('bug_type', models.CharField(choices=[('ERROR', 'Error'), ('FEATURE', 'New Feature'), ('ENHANCEMENT', 'Enhancement'), ('OTHER', 'Other')], default='ERROR', max_length=50)),
                ('report_date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('TO_DO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TO_DO', max_length=50)),
            ],
        ),
    ]
