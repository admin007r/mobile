# Generated by Django 5.0.1 on 2024-01-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bee',
            name='dec',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mobi',
            name='dec',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ucell',
            name='dec',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
