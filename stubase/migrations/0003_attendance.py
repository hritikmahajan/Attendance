# Generated by Django 3.1.7 on 2021-04-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stubase', '0002_auto_20210406_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('classandsec', models.CharField(max_length=5, unique=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
