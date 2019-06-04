from django.contrib import admin

from .models import MatchBySummoner, Match, TeamStatsByMatch, ParticipantStatsByMatch, StatsByParticipant

admin.site.register(MatchBySummoner)
admin.site.register(Match)
admin.site.register(TeamStatsByMatch)
admin.site.register(ParticipantStatsByMatch)
admin.site.register(StatsByParticipant)