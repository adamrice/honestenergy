from django.shortcuts import render
from django.utils import timezone
from .models import Offers


def offers_by_zip_list(request):
    """
    Obtains a list of offers given a zipcode using the `Offers` model.
    """
    description = '' # TODO(Mike): Fill in description
    title = '' # TODO(Mike): Fill in title
    offers = Offers.get_offers_by_zip(zipcode=request.zipcode)
    return render(
        request,
        'compengine/compare.html',
        {
            'offers': offers,
            'description': description,
            'title': title
        }
    )
