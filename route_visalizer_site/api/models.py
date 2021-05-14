from django.db import models


class Route(models.Model):
    """Model for saving the route data."""

    created_at = models.DateTimeField(auto_now=True)
    date_time = models.DateTimeField()


class GPSRecord(models.Model):
    """Model for saving GPS records data."""

    latitude = models.DecimalField(decimal_places=12, max_digits=15)
    longitude = models.DecimalField(decimal_places=12, max_digits=15)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)


class RouteAttributes(models.Model):
    """Model for saving the route attributes used for ML algs and searching"""

    max_speed = models.IntegerField()
    n_stops = models.IntegerField()
    len_km = models.DecimalField(decimal_places=2, max_digits=10)
    travel_time_s = models.IntegerField()
