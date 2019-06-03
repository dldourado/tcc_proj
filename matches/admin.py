from django.contrib import admin

from .models import MatchBySummoner, Match

admin.site.register(MatchBySummoner)
admin.site.register(Match)