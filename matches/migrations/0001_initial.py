# Generated by Django 2.2.2 on 2019-06-12 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('summoner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrameByMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasonId', models.PositiveIntegerField()),
                ('queueId', models.PositiveIntegerField()),
                ('gameId', models.CharField(max_length=128)),
                ('participantIdentities', models.TextField()),
                ('gameVersion', models.CharField(max_length=128)),
                ('platformId', models.CharField(max_length=128)),
                ('gameMode', models.CharField(max_length=128)),
                ('mapId', models.PositiveIntegerField()),
                ('gameType', models.CharField(max_length=128)),
                ('gameDuration', models.CharField(max_length=128)),
                ('gameCreation', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantStatsByMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participantId', models.IntegerField()),
                ('teamIsBlue', models.BooleanField()),
                ('spell1Id', models.IntegerField()),
                ('spell2Id', models.IntegerField()),
                ('highestAchievedSeasonTier', models.CharField(max_length=128)),
                ('championId', models.IntegerField()),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.Match')),
            ],
        ),
        migrations.CreateModel(
            name='TeamStatsByMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstDragon', models.BooleanField()),
                ('firstInhibitor', models.BooleanField()),
                ('bans', models.TextField()),
                ('baronKills', models.PositiveIntegerField()),
                ('firstRiftHerald', models.BooleanField()),
                ('firstBaron', models.BooleanField()),
                ('riftHeraldKills', models.PositiveIntegerField()),
                ('firstBlood', models.BooleanField()),
                ('teamIsBlue', models.BooleanField()),
                ('firstTower', models.BooleanField()),
                ('inhibitorKills', models.PositiveIntegerField()),
                ('towerKills', models.PositiveIntegerField()),
                ('win', models.BooleanField()),
                ('dragonKills', models.PositiveIntegerField()),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.Match')),
            ],
        ),
        migrations.CreateModel(
            name='StatsByParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magicDamageDealtToChampions', models.IntegerField()),
                ('damageDealtToObjectives', models.IntegerField()),
                ('damageDealtToTurrets', models.IntegerField()),
                ('physicalDamageDealtToChampions', models.IntegerField()),
                ('magicDamageDealt', models.IntegerField()),
                ('damageSelfMitigated', models.IntegerField()),
                ('magicalDamageTaken', models.IntegerField()),
                ('trueDamageTaken', models.IntegerField()),
                ('trueDamageDealt', models.IntegerField()),
                ('totalDamageTaken', models.IntegerField()),
                ('physicalDamageDealt', models.IntegerField()),
                ('totalDamageDealtToChampions', models.IntegerField()),
                ('physicalDamageTaken', models.IntegerField()),
                ('totalDamageDealt', models.IntegerField()),
                ('trueDamageDealtToChampions', models.IntegerField()),
                ('totalHeal', models.IntegerField()),
                ('perk0Var1', models.IntegerField()),
                ('perk0Var2', models.IntegerField()),
                ('perk0Var3', models.IntegerField()),
                ('perk1Var1', models.IntegerField()),
                ('perk1Var2', models.IntegerField()),
                ('perk1Var3', models.IntegerField()),
                ('perk2Var1', models.IntegerField()),
                ('perk2Var2', models.IntegerField()),
                ('perk2Var3', models.IntegerField()),
                ('perk3Var1', models.IntegerField()),
                ('perk3Var2', models.IntegerField()),
                ('perk3Var3', models.IntegerField()),
                ('perk4Var1', models.IntegerField()),
                ('perk4Var2', models.IntegerField()),
                ('perk4Var3', models.IntegerField()),
                ('perk5Var1', models.IntegerField()),
                ('perk5Var2', models.IntegerField()),
                ('perk5Var3', models.IntegerField()),
                ('perk0', models.IntegerField()),
                ('perk2', models.IntegerField()),
                ('perk1', models.IntegerField()),
                ('perk3', models.IntegerField()),
                ('perk4', models.IntegerField()),
                ('perk5', models.IntegerField()),
                ('perkPrimaryStyle', models.IntegerField()),
                ('perkSubStyle', models.IntegerField()),
                ('timeCCingOthers', models.IntegerField()),
                ('totalTimeCrowdControlDealt', models.IntegerField()),
                ('longestTimeSpentLiving', models.IntegerField()),
                ('firstBloodKill', models.BooleanField()),
                ('kills', models.IntegerField()),
                ('doubleKills', models.IntegerField()),
                ('tripleKills', models.IntegerField()),
                ('quadraKills', models.IntegerField()),
                ('pentaKills', models.IntegerField()),
                ('unrealKills', models.IntegerField()),
                ('killingSprees', models.IntegerField()),
                ('largestMultiKill', models.IntegerField()),
                ('largestKillingSpree', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('firstBloodAssist', models.BooleanField()),
                ('deaths', models.IntegerField()),
                ('playerScore0', models.IntegerField()),
                ('playerScore1', models.IntegerField()),
                ('playerScore2', models.IntegerField()),
                ('playerScore3', models.IntegerField()),
                ('playerScore4', models.IntegerField()),
                ('playerScore5', models.IntegerField()),
                ('playerScore6', models.IntegerField()),
                ('playerScore7', models.IntegerField()),
                ('playerScore8', models.IntegerField()),
                ('playerScore9', models.IntegerField()),
                ('totalScoreRank', models.IntegerField()),
                ('neutralMinionsKilled', models.IntegerField()),
                ('neutralMinionsKilledTeamJungle', models.IntegerField()),
                ('neutralMinionsKilledEnemyJungle', models.IntegerField()),
                ('totalMinionsKilled', models.IntegerField()),
                ('totalUnitsHealed', models.IntegerField()),
                ('largestCriticalStrike', models.IntegerField()),
                ('item0', models.IntegerField()),
                ('item1', models.IntegerField()),
                ('item2', models.IntegerField()),
                ('item3', models.IntegerField()),
                ('item4', models.IntegerField()),
                ('item5', models.IntegerField()),
                ('item6', models.IntegerField()),
                ('goldSpent', models.IntegerField()),
                ('goldEarned', models.IntegerField()),
                ('champLevel', models.IntegerField()),
                ('firstInhibitorKill', models.BooleanField()),
                ('inhibitorKills', models.IntegerField()),
                ('firstInhibitorAssist', models.BooleanField()),
                ('firstTowerAssist', models.BooleanField()),
                ('firstTowerKill', models.BooleanField()),
                ('turretKills', models.IntegerField()),
                ('combatPlayerScore', models.IntegerField()),
                ('participantId', models.IntegerField()),
                ('sightWardsBoughtInGame', models.IntegerField()),
                ('visionWardsBoughtInGame', models.IntegerField()),
                ('wardsPlaced', models.IntegerField()),
                ('wardsKilled', models.IntegerField()),
                ('totalPlayerScore', models.IntegerField()),
                ('visionScore', models.IntegerField()),
                ('objectivePlayerScore', models.IntegerField()),
                ('win', models.BooleanField()),
                ('participant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.ParticipantStatsByMatch')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantByFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalGold', models.IntegerField()),
                ('teamScore', models.IntegerField()),
                ('participantId', models.IntegerField()),
                ('level', models.IntegerField()),
                ('currentGold', models.IntegerField()),
                ('minionsKilled', models.IntegerField()),
                ('dominionScore', models.IntegerField()),
                ('position', models.CharField(max_length=40)),
                ('xp', models.IntegerField()),
                ('jungleMinionsKilled', models.IntegerField()),
                ('frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.FrameByMatch')),
            ],
        ),
        migrations.CreateModel(
            name='MatchBySummoner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lane', models.CharField(max_length=128)),
                ('gameId', models.CharField(max_length=128)),
                ('champion', models.PositiveIntegerField()),
                ('platformId', models.CharField(max_length=128)),
                ('season', models.PositiveIntegerField()),
                ('queue', models.PositiveIntegerField()),
                ('role', models.CharField(max_length=128)),
                ('timestamp', models.CharField(max_length=128)),
                ('summoner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='summoner.Summoner')),
            ],
        ),
        migrations.AddField(
            model_name='framebymatch',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.Match'),
        ),
        migrations.CreateModel(
            name='EventByFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(blank=True, max_length=64, null=True)),
                ('towerType', models.CharField(blank=True, max_length=64, null=True)),
                ('teamId', models.IntegerField(blank=True, null=True)),
                ('ascendedType', models.CharField(blank=True, max_length=64, null=True)),
                ('killerId', models.IntegerField(blank=True, null=True)),
                ('levelUpType', models.CharField(blank=True, max_length=64, null=True)),
                ('pointCaptured', models.CharField(blank=True, max_length=64, null=True)),
                ('assistingParticipantIds', models.CharField(blank=True, max_length=40, null=True)),
                ('wardType', models.CharField(blank=True, max_length=64, null=True)),
                ('monsterType', models.CharField(blank=True, max_length=64, null=True)),
                ('eType', models.CharField(blank=True, max_length=64, null=True)),
                ('skillSlot', models.IntegerField(blank=True, null=True)),
                ('victimId', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=128, null=True)),
                ('afterId', models.IntegerField(blank=True, null=True)),
                ('monsterSubType', models.CharField(blank=True, max_length=64, null=True)),
                ('laneType', models.CharField(blank=True, max_length=64, null=True)),
                ('itemId', models.IntegerField(blank=True, null=True)),
                ('participantId', models.IntegerField(blank=True, null=True)),
                ('buildingType', models.CharField(blank=True, max_length=64, null=True)),
                ('creatorId', models.IntegerField(blank=True, null=True)),
                ('position', models.CharField(blank=True, max_length=40, null=True)),
                ('beforeId', models.IntegerField(blank=True, null=True)),
                ('frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.FrameByMatch')),
            ],
        ),
    ]
