# Generated by Django 4.2.5 on 2023-09-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='stt',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='blog',
            table='Blog1',
        ),
    ]
