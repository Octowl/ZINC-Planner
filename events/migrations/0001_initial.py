# Generated by Django 2.1.7 on 2019-02-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
