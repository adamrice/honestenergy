from django import template


register = template.Library()

@register.simple_tag
def calculate_monthly_cost(rate):
    """
    This template tag computes the estimated monthly cost of energy based on
    the average kwh consumption of a US household.

    :param rate: float, the cost of energy / kwh
    :returns: str, formatted estimated monthly cost
    """
    # Avg US household consumes 901 kwh / month
    monthly_kwh_consumption = 901
    return '{0:.2f}'.format(
        rate * monthly_kwh_consumption
    )


@register.simple_tag
def calculate_rate_in_cents(rate):
    """
    This template tag computes the rate in cents.

    :param rate: float, the cost of energy / kwh
    :returns: str, formatted cost in cents
    """
    return '{0:.1f}'.format(
        rate * 100
    )


@register.simple_tag
def column_class_selector(index_, length):
    """
    This expects a column class selector in the format `[N]u 12u$([size])`
    Where `N` is a column number and size is the size of the screen using
    skel breakpoint selectors as seen here: https://github.com/ajlkn/skel/blob/master/docs/skel-layout.md#usage

    This tag should be used when looping through elements to render in HTML columns.
    The method parses the class and, depending on the lenght of the list,
    will assign a class.

    Expects that `index_` will start at 1 using django's `forloop.counter` as
    seen here: https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#for
    """
    class_ = "{num}u{end} 12u$(small)"

    # Logic for 3 column rows
    if length % 3 == 0:
        if index_ % 3 == 0:
            return class_.format(
                num='4',
                end='$'
            )
        else:
            return class_.format(
                num='4',
                end=''
            )

    # Logic for 2 column rows
    else:
        if index_ % 2 == 0:
            return class_.format(
                num='6',
                end='$'
            )
        else:
            return class_.format(
                num='6',
                end=''
            )
