# Generated by Django 2.2.5 on 2019-09-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_teacher_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Phonenumber',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
