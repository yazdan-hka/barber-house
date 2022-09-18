from tokenize import Special
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from BRAIDSTARZ.models import braiders


class register_form(FlaskForm):

    def validate_username(self, username_to_check):

        user = braiders.query.filter_by(username=username_to_check.data).first()

        if user:
            raise ValidationError(f'The Username "{user.username}" is unavailable. Please pick another one.')

    def validate_email(self, email_to_check):

        email = braiders.query.filter_by(email=email_to_check.data).first()

        if email:
            raise ValidationError(f'The Email {email.email} has been used. Please enter another one.')

    def validate_fullname(self, fullname_to_check):

        name = braiders.query.filter_by(fullname=fullname_to_check.data).first()

        if name:
            raise ValidationError(f'There is already an account with the name of "{name.fullname}". Please pick another one.')

    username = StringField(label='*Choose a Username ', validators=[DataRequired()])
    fullname = StringField(label='*Enter your full name ', validators=[DataRequired()])
    email = StringField(label='*Enter your Email Address: ', validators=[DataRequired()]) # Email(),
    password1 = PasswordField(label='*Enter a password: ', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='*Confirm your password: ', validators=[EqualTo('password1'), DataRequired()])
    phone_num = StringField(label='Enter your Phone number: ')
    country = StringField(label='*Enter your Country: ', validators=[DataRequired()])
    city = StringField(label='*Enter your city: ', validators=[DataRequired()])
    address = StringField(label='Enter the address of where you work: ', validators=[Length(max=512)])
    instagram = StringField(label='Enter your Instagram id: ')
    website = StringField(label='Enter your Website Address: ')
    twitter = StringField(label='Enter your Twitter id: ')
    tiktok = StringField(label='Enter your TikTok id: ')
    youtube = StringField(label='Enter your YouTube Channel: ')

    submit = SubmitField(label='Register')


class edit_braider_form(FlaskForm):


    def validate_username(self, username_to_check):

        user = braiders.query.filter_by(username=username_to_check.data).first()

        if user:
            raise ValidationError(f'The Username "{user.username}" is unavailable. Please pick another one.')

    def validate_email(self, email_to_check):

        email = braiders.query.filter_by(email=email_to_check.data).first()

        if email:
            raise ValidationError(f'The Email {email.email} has been used. Please enter another one.')

    def validate_fullname(self, fullname_to_check):

        name = braiders.query.filter_by(fullname=fullname_to_check.data).first()

        if name:
            raise ValidationError(f'There is already an account with the name of "{name.fullname}". Please pick another one.')

    username = StringField(label='Username: ', validators=[DataRequired()])
    fullname = StringField(label='Full name: ', validators=[DataRequired()])
    email = StringField(label='Email-address: ') # Email(),
    phone_num = StringField(label='Phone number: ')
    country = StringField(label='Country: ', validators=[DataRequired()])
    city = StringField(label='City: ', validators=[DataRequired()])
    address = StringField(label='Address: ', validators=[Length(max=512)])
    website = StringField(label='Enter your website address: ')
    instagram = StringField(label='Instagram id: ')
    twitter = StringField(label='Twitter id: ')
    tiktok = StringField(label='TikTok id: ')
    youtube = StringField(label='Youtube Channel: ')

    submit = SubmitField(label='Confirm changes')


class login_form(FlaskForm):

    username = StringField(label='Enter you username:', validators=[DataRequired()])
    password = PasswordField(label='Enter your password:', validators=[DataRequired()])
    submit = SubmitField(label='Log in')


class braider_finder_form(FlaskForm):

    search_content = StringField(label='Search..', validators=[Length(max=40), DataRequired()])
    submit = SubmitField(label='Find')


class email_messages_form(FlaskForm):

    name = StringField(label='Enter your name:', validators=[DataRequired()])
    email = StringField(label='Enter your Email-Address:', validators=[DataRequired()])
    message = StringField(label='Enter your message:a', validators=[DataRequired()])
    submit = SubmitField(label='Send')


class subscribe_form(FlaskForm):

    sub_email = StringField(label='Enter your email-address:', validators=[DataRequired() ]) # ,Email()
    submit = SubmitField(label='Subscribe')

    def validate_email(self, email_to_check):

        email = braiders.query.filter_by(email=email_to_check.data).first()

        if email:
            raise ValidationError(f'The Email {email.email} has been used. Please enter another one.')



class collection_filter_form(FlaskForm):

    styles = SelectField(u'Braid Styles', choices=[('All'), ('Box'), ('Dutch & French'), ('Goddes'), ('Crochet'), ('Cornrows'), ('Stitch'), ('Design')])
    under14 = SelectField(u'Under age 12 Styles(for kids)', choices=[ ('No'),('Yes')])
    special = SelectField(u'Special Designs', choices=[('No'), ('Yes')])

