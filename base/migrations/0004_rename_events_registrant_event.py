# Generated by Django 4.1.3 on 2022-11-21 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_registrant_student_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrant',
            old_name='events',
            new_name='event',
        ),
    ]
