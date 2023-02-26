from django.urls import path
from . import views

urlpatterns = [
    path('ml/<str:model_name>', views.predict),
]