# Generated by Django 4.0.4 on 2022-08-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]