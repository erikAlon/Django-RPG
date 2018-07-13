# Generated by Django 2.0.2 on 2018-03-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charactercreator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='energy',
        ),
        migrations.RemoveField(
            model_name='character',
            name='has_pet',
        ),
        migrations.RemoveField(
            model_name='character',
            name='mana',
        ),
        migrations.RemoveField(
            model_name='character',
            name='rage',
        ),
        migrations.AddField(
            model_name='cleric',
            name='mana',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='fighter',
            name='rage',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='mage',
            name='has_pet',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mage',
            name='mana',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='thief',
            name='energy',
            field=models.IntegerField(default=100),
        ),
    ]
