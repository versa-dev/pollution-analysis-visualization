from django.urls import path

from . import views

urlpatterns = [
    path('<pk>/', views.board_topics, name='board_topics'),
    path('<pk>/new/', views.new_topic, name='new_topic'),
]