# Generated by Django 3.0.5 on 2020-04-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foo', models.CharField(max_length=50)),
                ('bar', models.CharField(max_length=50)),
            ],
        ),
    ]
