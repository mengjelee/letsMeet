# Generated by Django 2.1.1 on 2018-11-29 09:23

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
                ('eventName', models.CharField(max_length=64)),
                ('dayChosen', models.CharField(max_length=20)),
                ('randUrl', models.CharField(max_length=20)),
            ],
        ),
    ]
