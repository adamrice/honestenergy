from django.shortcuts import render, redirect
from .forms import ZipcodeSearch
from compengine.views import offers_by_zip_list


def index(request):
    """
    Returns the homepage of the site.

    First checks whether or not the zipcode form is filled in.
    """
    # Check if a form was submitted
    if request.method == 'POST':
        zipcode_search_form = ZipcodeSearch(request.POST)
        if zipcode_search_form.is_valid():
            request.zipcode = zipcode_search_form.cleaned_data['zipcode']
            return offers_by_zip_list(request)

    else:
        zipcode_search_form = ZipcodeSearch()

    description = '' # TODO(Mike): Fill in description
    title = '' # TODO(Mike): Fill in title

    return render(
        request,
        'home/index.html',
        {
            'description': description,
            'title': title,
            'zipcode_search_form': zipcode_search_form,
        }
    )
