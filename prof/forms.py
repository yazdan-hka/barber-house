from django import forms
from django.core.exceptions import ValidationError

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
        widget=forms.Textarea(attrs={ 'id': 'exampleFormControlTextarea1', 'class': 'form-control'})
    )
    category = forms.ChoiceField(
        choices=braid_types,
        label='',
        # required=True,
        validators=[],
        widget=forms.Select(attrs={'id': 'category', 'class': 'form-select'})
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

    countries = (('', 'country'),
        ('Afghanistan', 'Afghanistan'),
        ('Aland Islands', 'Aland Islands'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('American Samoa', 'American Samoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antarctica', 'Antarctica'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Aruba', 'Aruba'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Bouvet Island', 'Bouvet Island'),
        ('Brazil', 'Brazil'),
        ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
        ('Brunei Darussalam', 'Brunei Darussalam'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Christmas Island', 'Christmas Island'),
        ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Congo, Democratic Republic of the Congo', 'Congo, Democratic Republic of the Congo'),
        ('Cook Islands', 'Cook Islands'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote D\'Ivoire', 'Cote D\'Ivoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Curacao', 'Curacao'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('French Guiana', 'French Guiana'),
        ('French Polynesia', 'French Polynesia'),
        ('French Southern Territories', 'French Southern Territories'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Greenland', 'Greenland'),
        ('Grenada', 'Grenada'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Guam', 'Guam'),
        ('Guatemala', 'Guatemala'),
        ('Guernsey', 'Guernsey'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Heard Island and Mcdonald Islands', 'Heard Island and Mcdonald Islands'),
        ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
        ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Isle of Man', 'Isle of Man'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jersey', 'Jersey'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea, Democratic People\'s Republic of', 'Korea, Democratic People\'s Republic of'),
        ('Korea, Republic of', 'Korea, Republic of'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macao', 'Macao'),
        ('Macedonia, the Former Yugoslav Republic of', 'Macedonia, the Former Yugoslav Republic of'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia, Federated States of', 'Micronesia, Federated States of'),
        ('Moldova, Republic of', 'Moldova, Republic of'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('Netherlands Antilles', 'Netherlands Antilles'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Island', 'Norfolk Island'),
        ('Northern Mariana Islands', 'Northern Mariana Islands'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Palestinian Territory, Occupied', 'Palestinian Territory, Occupied'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Pitcairn', 'Pitcairn'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Puerto Rico', 'Puerto Rico'),
        ('Qatar', 'Qatar'),
        ('Reunion', 'Reunion'),
        ('Romania', 'Romania'),
        ('Russian Federation', 'Russian Federation'),
        ('Rwanda', 'Rwanda'),
        ('Saint Barthelemy', 'Saint Barthelemy'),
        ('Saint Helena', 'Saint Helena'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Martin', 'Saint Martin'),
        ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Serbia and Montenegro', 'Serbia and Montenegro'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Sint Maarten', 'Sint Maarten'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syrian Arab Republic', 'Syrian Arab Republic'),
        ('Taiwan, Province of China', 'Taiwan, Province of China'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania, United Republic of', 'Tanzania, United Republic of'),
        ('Thailand', 'Thailand'),
        ('Timor-Leste', 'Timor-Leste'),
        ('Togo', 'Togo'),
        ('Tokelau', 'Tokelau'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('Viet Nam', 'Viet Nam'),
        ('Virgin Islands, British', 'Virgin Islands, British'),
        ('Virgin Islands, U.s.', 'Virgin Islands, U.s.'),
        ('Wallis and Futuna', 'Wallis and Futuna'),
        ('Western Sahara', 'Western Sahara'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),)

    def validate_username(value):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456_789'
        for i in value:
            if i not in chars:
                error_css_class = 'invalid-username'
                raise ValidationError(
                    f'Invalid Username "{value}". be sure that your username includes only capital and small '
                    'letters, numbers, and underscores(_).'.title(),
                    params={'value': value})

        if len(value) < 4:
            raise ValidationError(
                    f'Invalid Username "{value}". too shot username. minimum length is 4 character.'.title(),
                    params={'value': value})


    profile_picture = forms.ImageField(
        label='',
        required=False,
        help_text='Maximum file size is 2 MB',
        error_messages={
            'invalid': 'Please select a valid image file',
            'max_size': 'Please select a file smaller than 2 MB'
        },
        validators=[],
    )

    user_name = forms.CharField(
        max_length=27,
        label='',
        required=True,
        validators=[validate_username],
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

    country = forms.ChoiceField(
        choices=countries,
        label='',
        required=True,
        validators=[],
        # widget=forms.Select(attrs={})

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





