# Generated by Django 2.0.1 on 2018-06-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('auther', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=20)),
            ],
        ),
    ]
