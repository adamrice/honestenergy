from mailchimp3 import MailChimp
from django.conf import settings

def add_subscriber(email_address, zipcode, list_name='Leads'):
    """
    Adds a user to the specified mailchimp list.

    :param email_address: str, Email address of the subscriber
    :param first_name: str, First name of the subscriber
    :returns: mailchimp subscriber response object
    """
    client = MailChimp(settings.MAILCHIMP_USERNAME, settings.MAILCHIMP_SECRET_KEY)
    list_id = settings.MAILCHIMP_LISTS.get(list_name)

    client.lists.members.create(list_id, {
        'email_address': email_address,
        'status': 'subscribed',
        "merge_fields": {
          'ZIPCODE': zipcode,
        }
    })
