# Generated by Django 3.1.2 on 2020-11-02 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.DeleteModel(
            name='Business',
        ),
    ]
