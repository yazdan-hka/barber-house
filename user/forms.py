from django import forms
from django.core.exceptions import ValidationError
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.forms import AuthenticationForm
from main.models import Braider

class BraiderRegistration(forms.Form):

    def validate_insta_id(value):
        chars = '-=+][}{()!@#$%^&*|\?/\'<> ~`"'

        for i in chars:
            if i in value:
                raise ValidationError('Invalid Instagram ID. please enter a valid instgarm ID.'.title())
    def validate_password(value):

        number = '0123456789'
        chars = 'abcdefghijklmnopqrstuvwxyz'
        cap_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        wi = '!@#$%^&*()_-+={[}]|\\?/>,<.:;'
        password = value

        num = False
        char = False
        cap = False
        wierd = False
        le = False
        stars = ''

        if len(password) >= 8:
            le = True
        for i in number:
            if i in password:
                num = True
        for i in chars:
            if i in password:
                char = True
        for i in cap_chars:
            if i in password:
                cap = True
        for i in wi:
            if i in password:
                wierd = True

        if num or char:
            stars = '*'
        if num and char:
            stars = '**'
        if char and cap:
            stars += '*'
        if wierd:
            stars += '*'
        if le:
            stars += '*'

        if stars != '*****':
            raise ValidationError('your password is week. are you sure you used capital and small letters, numbers, '
                                  'and special characters in the length of 8 or more? '.title(),
                                  params={'value': value})
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
                    f'Invalid Username "{value}". too shot user name. minimum length is 4 character.'.title(),
                    params={'value': value})

    acc_types = (('c', 'Customer'), ('b', 'Braider'))
    phone_codes = (('+1', 'USA (+1)'),
                   ('+44', 'UK (+44)'),
                   ('+213', 'Algeria (+213)'),
                   ('+376', 'Andorra (+376)'),
                   ('+244', 'Angola (+244)'),
                   ('+1264', 'Anguilla (+1264)'),
                   ('+1268', 'Antigua &amp; Barbuda (+1268)'),
                   ('+54', 'Argentina (+54)'),
                   ('+374', 'Armenia (+374)'),
                   ('+297', 'Aruba (+297)'),
                   ('+61', 'Australia (+61)'),
                   ('+43', 'Austria (+43)'),
                   ('+994', 'Azerbaijan (+994)'),
                   ('+1242', 'Bahamas (+1242)'),
                   ('+973', 'Bahrain (+973)'),
                   ('+880', 'Bangladesh (+880)'),
                   ('+1246', 'Barbados (+1246)'),
                   ('+375', 'Belarus (+375)'),
                   ('+32', 'Belgium (+32)'),
                   ('+501', 'Belize (+501)'),
                   ('+229', 'Benin (+229)'),
                   ('+1441', 'Bermuda (+1441)'),
                   ('+975', 'Bhutan (+975)'),
                   ('+591', 'Bolivia (+591)'),
                   ('+387', 'Bosnia Herzegovina (+387)'),
                   ('+267', 'Botswana (+267)'),
                   ('+55', 'Brazil (+55)'),
                   ('+673', 'Brunei (+673)'),
                   ('+359', 'Bulgaria (+359)'),
                   ('+226', 'Burkina Faso (+226)'),
                   ('+257', 'Burundi (+257)'),
                   ('+855', 'Cambodia (+855)'),
                   ('+237', 'Cameroon (+237)'),
                   ('+1', 'Canada (+1)'),
                   ('+238', 'Cape Verde Islands (+238)'),
                   ('+1345', 'Cayman Islands (+1345)'),
                   ('+236', 'Central African Republic (+236)'),
                   ('+56', 'Chile (+56)'),
                   ('+86', 'China (+86)'),
                   ('+57', 'Colombia (+57)'),
                   ('+269', 'Comoros (+269)'),
                   ('+242', 'Congo (+242)'),
                   ('+682', 'Cook Islands (+682)'),
                   ('+506', 'Costa Rica (+506)'),
                   ('+385', 'Croatia (+385)'),
                   ('+53', 'Cuba (+53)'),
                   ('+90392', 'Cyprus North (+90392)'),
                   ('+357', 'Cyprus South (+357)'),
                   ('+42', 'Czech Republic (+42)'),
                   ('+45', 'Denmark (+45)'),
                   ('+253', 'Djibouti (+253)'),
                   ('+1809', 'Dominica (+1809)'),
                   ('+1809', 'Dominican Republic (+1809)'),
                   ('+593', 'Ecuador (+593)'),
                   ('+20', 'Egypt (+20)'),
                   ('+503', 'El Salvador (+503)'),
                   ('+240', 'Equatorial Guinea (+240)'),
                   ('+291', 'Eritrea (+291)'),
                   ('+372', 'Estonia (+372)'),
                   ('+251', 'Ethiopia (+251)'),
                   ('+500', 'Falkland Islands (+500)'),
                   ('+298', 'Faroe Islands (+298)'),
                   ('+679', 'Fiji (+679)'),
                   ('+358', 'Finland (+358)'),
                   ('+33', 'France (+33)'),
                   ('+594', 'French Guiana (+594)'),
                   ('+689', 'French Polynesia (+689)'),
                   ('+241', 'Gabon (+241)'),
                   ('+220', 'Gambia (+220)'),
                   ('+7880', 'Georgia (+7880)'),
                   ('+49', 'Germany (+49)'),
                   ('+233', 'Ghana (+233)'),
                   ('+350', 'Gibraltar (+350)'),
                   ('+30', 'Greece (+30)'),
                   ('+299', 'Greenland (+299)'),
                   ('+1473', 'Grenada (+1473)'),
                   ('+590', 'Guadeloupe (+590)'),
                   ('+671', 'Guam (+671)'),
                   ('+502', 'Guatemala (+502)'),
                   ('+224', 'Guinea (+224)'),
                   ('+245', 'Guinea - Bissau (+245)'),
                   ('+592', 'Guyana (+592)'),
                   ('+509', 'Haiti (+509)'),
                   ('+504', 'Honduras (+504)'),
                   ('+852', 'Hong Kong (+852)'),
                   ('+36', 'Hungary (+36)'),
                   ('+354', 'Iceland (+354)'),
                   ('+91', 'India (+91)'),
                   ('+62', 'Indonesia (+62)'),
                   ('+98', 'Iran (+98)'),
                   ('+964', 'Iraq (+964)'),
                   ('+353', 'Ireland (+353)'),
                   ('+972', 'Israel (+972)'),
                   ('+39', 'Italy (+39)'),
                   ('+1876', 'Jamaica (+1876)'),
                   ('+81', 'Japan (+81)'),
                   ('+962', 'Jordan (+962)'),
                   ('+7', 'Kazakhstan (+7)'),
                   ('+254', 'Kenya (+254)'),
                   ('+686', 'Kiribati (+686)'),
                   ('+850', 'Korea North (+850)'),
                   ('+82', 'Korea South (+82)'),
                   ('+965', 'Kuwait (+965)'),
                   ('+996', 'Kyrgyzstan (+996)'),
                   ('+856', 'Laos (+856)'),
                   ('+371', 'Latvia (+371)'),
                   ('+961', 'Lebanon (+961)'),
                   ('+266', 'Lesotho (+266)'),
                   ('+231', 'Liberia (+231)'),
                   ('+218', 'Libya (+218)'),
                   ('+417', 'Liechtenstein (+417)'),
                   ('+370', 'Lithuania (+370)'),
                   ('+352', 'Luxembourg (+352)'),
                   ('+853', 'Macao (+853)'),
                   ('+389', 'Macedonia (+389)'),
                   ('+261', 'Madagascar (+261)'),
                   ('+265', 'Malawi (+265)'),
                   ('+60', 'Malaysia (+60)'),
                   ('+960', 'Maldives (+960)'),
                   ('+223', 'Mali (+223)'),
                   ('+356', 'Malta (+356)'),
                   ('+692', 'Marshall Islands (+692)'),
                   ('+596', 'Martinique (+596)'),
                   ('+222', 'Mauritania (+222)'),
                   ('+269', 'Mayotte (+269)'),
                   ('+52', 'Mexico (+52)'),
                   ('+691', 'Micronesia (+691)'),
                   ('+373', 'Moldova (+373)'),
                   ('+377', 'Monaco (+377)'),
                   ('+976', 'Mongolia (+976)'),
                   ('+1664', 'Montserrat (+1664)'),
                   ('+212', 'Morocco (+212)'),
                   ('+258', 'Mozambique (+258)'),
                   ('+95', 'Myanmar (+95)'),
                   ('+264', 'Namibia (+264)'),
                   ('+674', 'Nauru (+674)'),
                   ('+977', 'Nepal (+977)'),
                   ('+31', 'Netherlands (+31)'),
                   ('+687', 'New Caledonia (+687)'),
                   ('+64', 'New Zealand (+64)'),
                   ('+505', 'Nicaragua (+505)'),
                   ('+227', 'Niger (+227)'),
                   ('+234', 'Nigeria (+234)'),
                   ('+683', 'Niue (+683)'),
                   ('+672', 'Norfolk Islands (+672)'),
                   ('+670', 'Northern Marianas (+670)'),
                   ('+47', 'Norway (+47)'),
                   ('+968', 'Oman (+968)'),
                   ('+680', 'Palau (+680)'),
                   ('+507', 'Panama (+507)'),
                   ('+675', 'Papua New Guinea (+675)'),
                   ('+595', 'Paraguay (+595)'),
                   ('+51', 'Peru (+51)'),
                   ('+63', 'Philippines (+63)'),
                   ('+48', 'Poland (+48)'),
                   ('+351', 'Portugal (+351)'),
                   ('+1787', 'Puerto Rico (+1787)'),
                   ('+974', 'Qatar (+974)'),
                   ('+262', 'Reunion (+262)'),
                   ('+40', 'Romania (+40)'),
                   ('+7', 'Russia (+7)'),
                   ('+250', 'Rwanda (+250)'),
                   ('+378', 'San Marino (+378)'),
                   ('+239', 'Sao Tome &amp; Principe (+239)'),
                   ('+966', 'Saudi Arabia (+966)'),
                   ('+221', 'Senegal (+221)'),
                   ('+381', 'Serbia (+381)'),
                   ('+248', 'Seychelles (+248)'),
                   ('+232', 'Sierra Leone (+232)'),
                   ('+65', 'Singapore (+65)'),
                   ('+421', 'Slovak Republic (+421)'),
                   ('+386', 'Slovenia (+386)'),
                   ('+677', 'Solomon Islands (+677)'),
                   ('+252', 'Somalia (+252)'),
                   ('+27', 'South Africa (+27)'),
                   ('+34', 'Spain (+34)'),
                   ('+94', 'Sri Lanka (+94)'),
                   ('+290', 'St. Helena (+290)'),
                   ('+1869', 'St. Kitts (+1869)'),
                   ('+1758', 'St. Lucia (+1758)'),
                   ('+249', 'Sudan (+249)'),
                   ('+597', 'Suriname (+597)'),
                   ('+268', 'Swaziland (+268)'),
                   ('+46', 'Sweden (+46)'),
                   ('+41', 'Switzerland (+41)'),
                   ('+963', 'Syria (+963)'),
                   ('+886', 'Taiwan (+886)'),
                   ('+7', 'Tajikstan (+7)'),
                   ('+66', 'Thailand (+66)'),
                   ('+228', 'Togo (+228)'),
                   ('+676', 'Tonga (+676)'),
                   ('+1868', 'Trinidad &amp; Tobago (+1868)'),
                   ('+216', 'Tunisia (+216)'),
                   ('+90', 'Turkey (+90)'),
                   ('+7', 'Turkmenistan (+7)'),
                   ('+993', 'Turkmenistan (+993)'),
                   ('+1649', 'Turks &amp; Caicos Islands (+1649)'),
                   ('+688', 'Tuvalu (+688)'),
                   ('+256', 'Uganda (+256)'),
                   ('+44', 'UK (+44)'),
                   ('+380', 'Ukraine (+380)'),
                   ('+971', 'United Arab Emirates (+971)'),
                   ('+598', 'Uruguay (+598)'),
                   ('+1', 'USA (+1)'),
                   ('+7', 'Uzbekistan (+7)'),
                   ('+678', 'Vanuatu (+678)'),
                   ('+379', 'Vatican City (+379)'),
                   ('+58', 'Venezuela (+58)'),
                   ('+84', 'Vietnam (+84)'),
                   ('+84', 'Virgin Islands - British (+1284)'),
                   ('+84', 'Virgin Islands - US (+1340)'),
                   ('+681', 'Wallis &amp; Futuna (+681)'),
                   ('+969', 'Yemen (North)(+969)'),
                   ('+967', 'Yemen (South)(+967)'),
                   ('+260', 'Zambia (+260)'),
                   ('+263', 'Zimbabwe (+263)'),)
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

    first_name = forms.CharField(
        max_length=30,
        strip=False,
        label='',
        required=True,
        validators=[],
        widget=forms.TextInput(attrs={'class': 'text', 'placeholder': 'Firstname'})
    )
    last_name = forms.CharField(
        strip=False,
        label='',
        required=True,
        validators=[],
        widget=forms.TextInput(attrs={'class': 'text', 'placeholder': 'Lastname'})
    )
    user_type = forms.ChoiceField(
        choices=acc_types,
        required=True,
        label='',
        widget=forms.Select(attrs={'class': 'form-select email text-1', 'aria-label': 'Default select example'})
    )
    user_name = forms.CharField(
        max_length=27,
        strip=True,
        label='',
        required=True,
        validators=[validate_username],
        widget=forms.TextInput(attrs={'class': 'text', 'placeholder': 'Username(no white space)'})
    )
    insta_id = forms.CharField(
        max_length=40,
        strip=True,
        label='',
        required=False,
        validators=[],
        widget=forms.TextInput(attrs={'class': 'text', 'placeholder': 'Your Instagram ID'})
    )
    website = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Your Website'})
    )
    email = forms.EmailField(
        required=True,
        max_length=254,
        label='',
        widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Email Address'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'pass', 'placeholder': 'Password'}),
        required=True,
        max_length=120,
        min_length=8,
        validators=[validate_password]
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'pass', 'placeholder': 'Repeat Password'}),
        required=True,
        max_length=120,
        min_length=8,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'text', 'placeholder': 'Repeat Password'}),
        required=False,
        max_length=120,
        min_length=8,
    )
    phone_code = forms.ChoiceField(
        choices=phone_codes,
        label='',
        required=True,
        widget=forms.Select(attrs={'class': 'code', 'aria-label': 'Default select example'})
    )
    phone_number = forms.CharField(
        min_length=5,
        max_length=15,
        label='',
        required=True,
        widget=forms.TextInput(attrs={'class': 'number', 'placeholder': 'Phone Number'})
    )
    country = forms.ChoiceField(
        choices=countries,
        label='',
        required=True,
        widget=forms.Select(attrs={'class': 'form-select text-1', 'aria-label': 'Default select example'}))
    city = forms.CharField(
        max_length=50,
        strip=False,
        label='',
        required=True,
        validators=[],
        widget=forms.TextInput(attrs={'class': ' text-1', 'placeholder': 'City'})
    )

    def clean(self):
        cleaned_data = super().clean()

        # Phone Number
        code = cleaned_data.get('phone_code')
        num = cleaned_data.get('phone_number')

        # modify the field data as desired
        code_num = code + num

        # update the cleaned_data dictionary with the modified data
        cleaned_data['phone_number'] = code_num

        # Password Validation
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('password2')

        if pass2 == pass1 and pass2:
            cleaned_data['password'] = pass1
        else:
            raise ValidationError('Error. passwords are not the same. Try again.'.title())
        return cleaned_data

class BraiderLogin(forms.Form):
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
                    f'Invalid Username "{value}". too shot user name. minimum length is 4 character.'.title(),
                    params={'value': value})

    def validate_password(value):
        if len(value) < 8:
            raise ValidationError('your password is less than 8 characters. enter again.'.title())


    username = forms.CharField(
        max_length=27,
        strip=False,
        label='',
        required=True,
        validators=[validate_username],
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username or Email', 'class': 'text'})
    )
    password = forms.CharField(
        strip=False,
        required=True,
        validators=[],
        max_length=120,
        min_length=8,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'pass', 'placeholder': 'Password'}),
    )
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'flexCheckDefault'}),
        required=False
    )





