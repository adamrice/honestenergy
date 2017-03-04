from django.shortcuts import render

from .models import Offers, PotentialCustomers
from .forms import PotentialCustomersEmail

from honestenergy.contrib.mailchimp_helper import add_subscriber


def offers_by_zip_list(request):
    """
    Obtains a list of offers given a zipcode using the `Offers` model.
    """
    if request.method == 'POST':
        email_entry_form = PotentialCustomersEmail(request.POST)
        if email_entry_form.is_valid():
            zipcode=request.zipcode
            email=email_entry_form.cleaned_data['email']

            # Save potential customer to database
            PotentialCustomers.add_potential_customer(
                email=email,
                zipcode=zipcode
            )

            # Add potential customer to mailchimp
            add_subscriber(
                email,
                zipcode,
                list_name='Leads'
            )

    description = '' # TODO(Mike): Fill in description
    title = '' # TODO(Mike): Fill in title
    offers = Offers.get_offers_by_zip(zipcode=request.zipcode)
    email_entry_form = PotentialCustomersEmail()
    return render(
        request,
        'compengine/compare.html',
        {
            'offers': offers,
            'description': description,
            'title': title,
            'input_zipcode': request.zipcode,
            'email_entry_form': email_entry_form,
        }
    )
