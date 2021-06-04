from django.urls import path
import api.views as views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("routes/", views.RouteView.as_view(), name="test"),
    path("login/", obtain_auth_token, name="login"),
]
