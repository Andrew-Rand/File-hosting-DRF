# Generated by Django 3.2.7 on 2021-09-30 06:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_alive', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=250)),
                ('file', models.FileField(blank=True, upload_to='files')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
