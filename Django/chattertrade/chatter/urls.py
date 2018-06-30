from django.urls import path

from . import views

urlpatterns = [
    # ex:
    path('', views.index, name='index'),
    path('currencies/<room_name>', views.get_room, name='Room Name')
]
