# Generated by Django 4.1.3 on 2022-11-21 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_registrant_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registrant',
            unique_together={('event', 'student_id', 'last_name', 'first_name')},
        ),
    ]
