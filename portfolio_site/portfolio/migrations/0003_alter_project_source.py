# Generated by Django 4.0 on 2021-12-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='source',
            field=models.URLField(),
        ),
    ]