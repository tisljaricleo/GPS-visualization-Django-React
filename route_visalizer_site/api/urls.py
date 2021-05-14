from django.urls import path
import api.views as views


urlpatterns = [
    path("routes/", views.RouteView.as_view(), name="test"),
]
