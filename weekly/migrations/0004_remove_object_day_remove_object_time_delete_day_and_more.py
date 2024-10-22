# Generated by Django 4.2.3 on 2023-10-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekly', '0003_day_time_remove_object_day_remove_object_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='day',
        ),
        migrations.RemoveField(
            model_name='object',
            name='time',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
        migrations.AddField(
            model_name='object',
            name='day',
            field=models.CharField(choices=[('saturday', 'Saturday'), ('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wensday', 'Wensday'), ('thursday', 'Thursday'), ('friday', 'Friday')], default='saturday', max_length=200),
        ),
        migrations.AddField(
            model_name='object',
            name='time',
            field=models.CharField(choices=[('9-10:30', '9-10:30'), ('10:30-12', '10:30-12'), ('13-15', '13-15'), ('15-17', '15-17'), ('17-19', '17-19')], default='9-10:30', max_length=200),
        ),
    ]
