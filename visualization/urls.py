from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('player/',views.player, name='player'),
    path('get_match/',views.get_match, name='get_match'),
    path('get_player/',views.get_player, name='get_player'),
]