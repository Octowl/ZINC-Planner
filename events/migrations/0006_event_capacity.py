# Generated by Django 2.1.7 on 2019-02-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.IntegerField(default=1),
        ),
    ]