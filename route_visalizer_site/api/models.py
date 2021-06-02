from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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
