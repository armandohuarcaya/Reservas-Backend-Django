# Generated by Django 2.1.5 on 2019-03-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('estado', models.IntegerField(max_length=1)),
            ],
        ),
    ]
