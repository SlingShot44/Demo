from django.urls import path
from .views import view

app_name = 'DemoApp'

urlpatterns = [
    path('', view, name='index')
]