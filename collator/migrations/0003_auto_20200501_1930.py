# Generated by Django 3.0.5 on 2020-05-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collator', '0002_auto_20200419_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawflag',
            name='reported_user_id',
            field=models.CharField(max_length=25),
        ),
    ]