# Generated by Django 2.0.5 on 2018-05-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0009_auto_20180516_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('H', 'H'), ('M', 'M')], max_length=2),
        ),
    ]
