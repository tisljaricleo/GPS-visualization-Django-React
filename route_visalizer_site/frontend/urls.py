from django.urls import path
import frontend.views as views

urlpatterns = [
    path("", views.index),
    path("second", views.index),
]
