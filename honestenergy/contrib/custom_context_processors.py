from django.conf import settings


def keychain(request):
    """
    A context manager that adds various configuraiton keys and IDs to
    the site's context. This allows templates to access their values.
    This allows us to organize all of them in the settings module and have
    the site access them dynamically.
    """
    context_additions = {
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
    }

    return context_additions
