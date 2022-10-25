# Generated by Django 4.1.2 on 2022-10-18 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0033_repair_repairrequesttoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairdetail',
            name='repairEstimateTime',
            field=models.TimeField(blank=True, default='23:09:42'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repairDesc',
            field=models.TextField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repairSummary',
            field=models.CharField(default='-', max_length=500),
        ),
    ]
