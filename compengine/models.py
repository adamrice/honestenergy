from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Offers(models.Model):
    """
    The dimensional table that houses offers esco by zip/zone and utility.

    ESCO is an Energy Services Company such as CCE
    Utility is a utility company such as ConEd
    """
    # Offer location details
    zipcode = models.IntegerField()
    load_zone = models.CharField(max_length=256)

    # Utility Details
    utility_name = models.CharField(max_length=256)
    utility_short_name = models.CharField(max_length=256)

    # Esco / offer details
    esco = models.CharField(max_length=256)
    commodity = models.CharField(max_length=256)
    offer_type = models.CharField(max_length=256)
    active = models.BooleanField()
    rate_kwh = models.FloatField() # in $ / kwh
    green = models.BooleanField()
    minimum_term = models.CharField(max_length=256)
    has_cancellation_fee = models.BooleanField()
    cancellation_fee = models.FloatField(null=True) # in $
    dt_created = models.DateTimeField()
    dt_updated = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_offers_by_zip(cls, zipcode):
        """
        Uses the django ORM to obtain offers for a given zipcode.
        """
        offers_by_zip = cls.objects.filter(
            zipcode__exact=zipcode,
            active__exact=True,
            green__exact=True)

        return offers_by_zip
