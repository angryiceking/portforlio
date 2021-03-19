# Generated by Django 2.2.12 on 2020-09-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvp', '0005_auto_20200904_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiddenskillpotential',
            name='skill_damage',
            field=models.FloatField(default=420, unique=True),
        ),
        migrations.AlterField(
            model_name='skillone',
            name='skill_damage',
            field=models.FloatField(default=34, unique=True),
        ),
        migrations.AlterField(
            model_name='skillpassive',
            name='skill_damage',
            field=models.FloatField(default=52, unique=True),
        ),
        migrations.AlterField(
            model_name='skillthree',
            name='skill_damage',
            field=models.FloatField(default=297, unique=True),
        ),
        migrations.AlterField(
            model_name='skilltwo',
            name='skill_damage',
            field=models.FloatField(default=77, unique=True),
        ),
        migrations.AlterField(
            model_name='skillult',
            name='skill_damage',
            field=models.FloatField(default=235, unique=True),
        ),
    ]