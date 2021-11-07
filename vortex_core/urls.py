from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('briefing', views.briefing, name='briefing'),
    path('send_application', views.send_application, name='send_application'),
]