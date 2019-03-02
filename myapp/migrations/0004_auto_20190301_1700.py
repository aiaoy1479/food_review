# Generated by Django 2.1.5 on 2019-03-01 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190221_0400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AddField(
            model_name='review',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Shop'),
        ),
        migrations.AddField(
            model_name='shop',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]