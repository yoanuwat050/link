# Generated by Django 4.1 on 2022-09-15 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import randomslugfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repairStatusName', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='RepairType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repairTypeName', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='RepairStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repairStaffName', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('userStaff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RepairDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repairDetail', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('repairType', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repair.repairtype')),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repairCause', models.CharField(max_length=500)),
                ('repairDesc', models.CharField(default='Nothing', max_length=500)),
                ('repairSummary', models.CharField(default='Nothing', max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('recieve_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('work_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('done_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('slug', randomslugfield.fields.RandomSlugField(blank=True, editable=False, length=7, max_length=7, unique=True)),
                ('repairDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repair.repairdetail')),
                ('repairStaff', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='repair.repairstaff')),
                ('repairStatus', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='repair.repairstatus')),
            ],
        ),
        migrations.CreateModel(
            name='EmpUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empCID', models.CharField(max_length=13)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('empUser', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]