# Generated by Django 2.1.5 on 2019-07-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_auto_20190727_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogos',
            name='estado',
            field=models.CharField(max_length=1),
        ),
    ]
