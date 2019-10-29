from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('player/',views.player, name='player'),
    path('get_match/',views.get_match, name='get_match'),
    path('get_player/',views.get_player, name='get_player'),
    path('champions_network/',views.champions_network, name='champions_network'),
    path('stats_treemap/',views.stats_treemap, name='stats_treemap'),
]