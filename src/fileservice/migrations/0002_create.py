from django.db import migrations


def load_data(apps, shema_editor):
    FileStorage = apps.get_model('fileservice', 'FileStorage')

    FileStorage(type='temp', destination='/usr/src/app/storage/temp/').save()
    FileStorage(type='permanent', destination='/usr/src/app/storage/permanent/').save()


class Migration(migrations.Migration):
    dependencies = [
        ('fileservice', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
