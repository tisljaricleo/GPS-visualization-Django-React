from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import api.serializers as serializers
import api.models as models


class RouteView(generics.ListCreateAPIView):
    """View for get and set the routes"""

    permission_classes = [IsAuthenticated]

    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
