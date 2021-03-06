# Generated by Django 3.0.8 on 2020-07-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200729_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='Name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='state',
            name='Name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
