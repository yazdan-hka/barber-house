from django import forms
from .models import PostedMedia
from main.models import Braider


braid_types = (
    ('others', 'others'),
    ('Box Braids', 'Box Braids'),
    ('Cornrows', 'Cornrows'),
    ('Crochet Braids', 'Crochet Braids'),
    ('Dreadlocks', 'Dreadlocks'),
    ('Faux Locs', 'Faux Locs'),
    ('Goddess Braids', 'Goddess Braids'),
    ('Havana Twists', 'Havana Twists'),
    ('Kinky Twists', 'Kinky Twists'),
    ('Marley Twists', 'Marley Twists'),
    ('Micro Braids', 'Micro Braids'),
    ('Senegalese Twists', 'Senegalese Twists'),
    ('Tree Braids', 'Tree Braids'),
    ('Waterfall Braids', 'Waterfall Braids'),
    ('Yarn Braids', 'Yarn Braids'),
    ('Weaves', 'Weaves'),

)

class PictureForm(forms.Form):

    desc = forms.CharField(
        max_length=81,
        label='',
        # required=True,
        validators=[],
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )
    catg = forms.ChoiceField(
        choices=braid_types,
        label='',
        # required=True,
        validators=[],
        widget=forms.Select(attrs={'autofocus': True, 'placeholder': 'Category', 'class': 'text'})
    )
    pict = forms.ImageField()
