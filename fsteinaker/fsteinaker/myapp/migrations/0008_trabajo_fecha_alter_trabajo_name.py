# Generated by Django 4.2.6 on 2023-12-01 23:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_trabajo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='fecha',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]