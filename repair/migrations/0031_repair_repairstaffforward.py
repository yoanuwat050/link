# Generated by Django 4.1 on 2022-09-22 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0030_delete_empuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='repairStaffForward',
            field=models.CharField(default='Nothing', max_length=100),
        ),
    ]
