from django.shortcuts import render
from rest_framework import generics
import api.serializers as serializers
import api.models as models


class RouteView(generics.ListCreateAPIView):
    """View for get and set the routes"""

    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
