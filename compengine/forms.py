from django import forms


class PotentialCustomersEmail(forms.Form):
    """
    An instance of a django form meant to handle an email input by the user.
    This form is only displayed if the user searched for their zipcode and
    we do not currently have any offers in their area.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'id':'email',
                'name': 'email',
                'placeholder': 'Email',
                'type': 'email',
            }
        )
    )
