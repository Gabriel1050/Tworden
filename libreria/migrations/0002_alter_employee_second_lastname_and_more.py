# Generated by Django 4.0.6 on 2022-08-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='second_lastname',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='second_name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]