# Generated by Django 4.1.2 on 2022-10-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0009_empuser_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empTypeName', models.CharField(max_length=100)),
            ],
        ),
    ]
