# Generated by Django 3.0.5 on 2021-01-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210124_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyconversation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pyfriends',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pypublication',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
