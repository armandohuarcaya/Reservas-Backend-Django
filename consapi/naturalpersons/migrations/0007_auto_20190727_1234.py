# Generated by Django 2.1.5 on 2019-07-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naturalpersons', '0006_auto_20190727_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naturalpersons',
            name='celular',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='naturalpersons',
            name='dni',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='naturalpersons',
            name='estado',
            field=models.CharField(max_length=1),
        ),
    ]
