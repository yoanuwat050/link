# Generated by Django 4.1 on 2022-09-17 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repair', '0007_remove_repair_repairrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='repairStaff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
