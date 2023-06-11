from django import forms
from .models import Message
class BraiderFinder(forms.Form):

    search = forms.CharField(
        max_length=40,
        min_length=2,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search..', 'aria-label': "Recipient's username", 'aria-describedby':"button-addon2"})
    )

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'message': 'Message',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }