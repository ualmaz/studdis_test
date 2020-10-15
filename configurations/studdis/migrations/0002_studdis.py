from django.db import migrations

def create_data(apps, schema_editor):
    Student = apps.get_model('studdis', 'Student')
    Student(first_name="Student 001", last_name="Student 001", email="student001@email.com", phone="0700565656", address="Student 000 Address").save()


class Migration(migrations.Migration):

    dependencies = [
        ('studdis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]




