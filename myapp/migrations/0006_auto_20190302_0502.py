# Generated by Django 2.1.5 on 2019-03-02 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190301_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='shop',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
