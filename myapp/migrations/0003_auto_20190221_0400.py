# Generated by Django 2.1.5 on 2019-02-21 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190220_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='cate',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='menu',
        ),
        migrations.AddField(
            model_name='cate',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Shop'),
        ),
        migrations.AddField(
            model_name='menu',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Shop'),
        ),
    ]
