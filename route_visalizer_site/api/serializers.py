from django.db.models import fields
from rest_framework import serializers
import api.models as models


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = ["id", "created_at", "date_time"]


class GPSRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GPSRecord
        fields = ["id", "latitude", "longitude", "route_id"]


class RouteAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RouteAttributes
        fields = ["id", "max_speed", "n_stops", "len_km", "travel_time_s"]
