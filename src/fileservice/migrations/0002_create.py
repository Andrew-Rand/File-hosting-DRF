from django.db import migrations


def load_data(apps, shema_editor):
    FileStorage = apps.get_model('files', 'FileStorage')

    FileStorage(type='temp', destination='storage/temp/').save()
    FileStorage(type='permanent', destination='storage/permanent/').save()


class Migration(migrations.Migration):
    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
