# Generated by Django 3.0.5 on 2020-05-15 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userspermissions', '0005_remove_role_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
        migrations.CreateModel(
            name='RoleProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('roles', models.ManyToManyField(to='userspermissions.Role')),
            ],
        ),
    ]
