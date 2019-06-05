# Generated by Django 2.2.2 on 2019-06-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0008_auto_20190604_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventbyframe',
            name='afterId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='ascendedType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='assistingParticipantIds',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='beforeId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='buildingType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='creatorId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='eType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='eventType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='itemId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='killerId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='laneType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='levelUpType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='monsterSubType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='monsterType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='participantId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='pointCaptured',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='position',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='skillSlot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='teamId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='timestamp',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='towerType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='victimId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventbyframe',
            name='wardType',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
