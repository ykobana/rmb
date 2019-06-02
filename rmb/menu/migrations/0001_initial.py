# Generated by Django 2.1 on 2019-02-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('name', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=256)),
            ],
        ),
    ]
