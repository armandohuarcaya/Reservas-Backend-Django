# Generated by Django 2.1.5 on 2019-07-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogos',
            name='estado',
            field=models.IntegerField(verbose_name=1),
        ),
    ]
