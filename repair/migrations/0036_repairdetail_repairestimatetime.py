# Generated by Django 4.1.2 on 2022-10-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0035_remove_repairdetail_repairestimatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairdetail',
            name='repairEstimateTime',
            field=models.TimeField(default='00:09:42'),
        ),
    ]
