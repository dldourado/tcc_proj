from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('get_match/',views.get_match, name='get_match'),
]