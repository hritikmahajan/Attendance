# Generated by Django 3.1.7 on 2021-04-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stubase', '0004_auto_20210406_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='classandsec',
            field=models.CharField(max_length=5),
        ),
    ]
