# Generated by Django 3.2.5 on 2021-09-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='clss',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='language',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject',
            field=models.IntegerField(),
        ),
    ]
