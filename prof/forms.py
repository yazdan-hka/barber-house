from django import forms


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

    description = forms.CharField(
        max_length=81,
        label='',
        # required=True,
        validators=[],
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )
    category = forms.ChoiceField(
        choices=braid_types,
        label='',
        # required=True,
        validators=[],
        widget=forms.Select(attrs={'autofocus': True, 'placeholder': 'Category', 'class': 'text'})
    )
    image = forms.ImageField(
        label='Choose an image',
        required=True,
        help_text='Maximum file size is 2 MB',
        error_messages={
            'required': 'This field is required',
            'invalid': 'Please select a valid image file',
            'max_size': 'Please select a file smaller than 2 MB'
        },
        validators=[],
        widget=forms.ClearableFileInput(attrs={'style': 'color:white;'})
    )

class EditProfile(forms.Form):
    user_name = forms.CharField(
        max_length=27,
        label='',
        required=True,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    first_name = forms.CharField(
        max_length=23,
        label='',
        required=True,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    last_name = forms.CharField(
        max_length=22,
        label='',
        required=True,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    instagram = forms.URLField(
        max_length=234,
        label='',
        required=False,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    twitter = forms.URLField(
        max_length=234,
        label='',
        required=False,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    facebook = forms.URLField(
        max_length=234,
        label='',
        required=False,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    youtube = forms.URLField(
        max_length=234,
        label='',
        required=False,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    tiktok = forms.URLField(
        max_length=234,
        label='',
        required=False,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    country = forms.CharField(
        max_length=27,
        label='',
        required=True,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    city = forms.CharField(
        max_length=81,
        label='',
        required=True,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    website = forms.URLField(
        max_length=234,
        label='',
        required=False,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )

    business_name = forms.CharField(
        max_length=81,
        label='',
        required=False,
        validators=[],
        # widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Description', 'class': 'text'})
    )





