from django.shortcuts import render
from django.utils import timezone
from .models import Offers


def offers_by_zip_list(request):
    """
    Obtains a list of offers given a zipcode using the `Offers` model.
    """
    offers = Offers.get_offers_by_zip(zipcode=request.zipcode) # TODO(Mike): update zipcode extraction from request

    return render(request, 'blog/post_list.html', {'offers': offers}) # TODO(Mike): update template
