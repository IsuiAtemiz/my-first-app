# Generated by Django 2.0.5 on 2018-05-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0006_auto_20180516_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='puesto',
            field=models.CharField(max_length=5),
        ),
    ]
