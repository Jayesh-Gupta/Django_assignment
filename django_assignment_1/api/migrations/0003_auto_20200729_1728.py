# Generated by Django 3.0.8 on 2020-07-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200729_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='Name',
            field=models.CharField(editable=False, max_length=100, unique=True),
        ),
    ]
