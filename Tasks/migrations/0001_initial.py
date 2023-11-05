# Generated by Django 4.2.7 on 2023-11-03 10:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lists', '0001_initial'),
        ('Priorities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('isDone', models.BooleanField(default=False)),
                ('dateCreated', models.DateTimeField(default=datetime.datetime(2023, 11, 3, 12, 42, 40, 760754))),
                ('dateDue', models.DateTimeField(null=True)),
                ('dateCompleted', models.DateTimeField(null=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lists.listmodel')),
                ('priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Priorities.prioritymodel')),
            ],
        ),
    ]