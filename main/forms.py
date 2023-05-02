from django import forms

class BraiderFinder(forms.Form):

    search = forms.CharField(
        max_length=40,
        min_length=2,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search..', 'aria-label': "Recipient's username", 'aria-describedby':"button-addon2"})
    )



