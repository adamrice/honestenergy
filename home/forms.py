from django import forms


class ZipcodeSearch(forms.Form):
    """
    An instance of a django form meant to handle a zipcode input by the user.
    This input will eventually be used to search the database for offers
    that match the user's zipcode.
    """

    zipcode = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'id':'name',
                'placeholder': 'Zip Code',
            }
        )
    )
