# Generated by Django 4.1 on 2022-09-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='descripcion',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
