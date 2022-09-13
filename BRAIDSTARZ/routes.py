from BRAIDSTARZ import app, db
from flask import render_template, redirect, url_for, flash, request
from BRAIDSTARZ.models import braiders, email_messages, subscribers
from BRAIDSTARZ.forms import register_form, login_form, braider_finder_form, email_messages_form, subscribe_form, edit_braider_form, collection_filter_form
from flask_login import login_user, current_user, logout_user
from BRAIDSTARZ.func import find_braiders, subscribe, authenticated
import smtplib, ssl
import random
from time import sleep
from email.message import EmailMessage



@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])
def home_page():

    search_form = braider_finder_form()
    name = 'BRAIDSTARZ'
    true_user = False

    sub_form = subscribe_form()
    subscribe(sub_form)

    images = []
    i = 1

    while i <= 78:

        images.append(f'normal-design ({i})')

        i = i + 1

    name, loged_in, true_user = authenticated(current_user, true_user, name)

    if search_form.validate_on_submit():

        searched = search_form.search_content.data
        results = find_braiders(db, searched, braiders)

        if results is False:

            flash(f'No matches for your search. try again.', category='danger')
        else:

            return render_template('home.html', search=search_form, braider=results, sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user,images=images)

    return render_template('home.html', search=search_form, sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user,images=images)


@app.route('/about', methods=['GET', 'POST'])
def about_page():

    name = 'BRAIDSTARZ'
    true_user = False
    
    sub_form = subscribe_form()
    subscribe(sub_form)

    name, loged_in , true_user= authenticated(current_user, true_user, name)

    return render_template('about.html', sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user)


@app.route('/login', methods=['GET', 'POST'])
def login_page():


    form = login_form()
    sub_form = subscribe_form()
    subscribe(sub_form)

    if form.validate_on_submit():
        attempted_user = braiders.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are in your account dear {attempted_user.fullname}', category='success')

            return redirect(url_for('home_page'))

        else:
            flash(f'Error! wrong username or password.', category='danger')

    return render_template('login.html', form=form, sub_form=sub_form)

verified = True

@app.route('/ToBeConfirmed/<code>', methods=['GET'])
def to_be_confirmed(code):


    visited = braiders.query.filter_by(token=code).first_or_404()
    if visited:
        visited.confirmed = True
        db.session.commit()
        flash(f'Success! your account has been created successfully', category='success')

    return redirect(url_for('home_page'))


def verify_email(email, code):

    email_sender = 'yazdan.unknown@gmail.com'
    email_password = 'nhdcubwbvjzpppss'
    email_receiver = email

    subject = ''
    body = f"""\
    Subject: BraidStarz
    Hey! Welcome to BraidStarz Family..

    Click on the Link Bellow to Confirm Your Registration.

    https://www.braidstarz.art/ToBeConfirmed/{code}
    """
    em = EmailMessage()
    em['BraidStarz'] = email_sender
    em['To'] = email_receiver
    em['Email Verification'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print('email is sent')
    

@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = register_form()
    sub_form = subscribe_form()

    if sub_form.validate_on_submit():

        if subscribers.query.filter_by(email=sub_form.email.data).first():

            flash(f'The email {sub_form.email.data} has been subscribed. Please enter another email-address. ', category='danger')

        else:
            new_sub = subscribers(email=sub_form.email.data)
            db.session.add(new_sub)
            db.session.commit()

            flash('You subscribed successfully!', category='success')

            return render_template('register.html', form=form, sub_form=sub_form)

    if form.validate_on_submit():
    
        if form.address.data.lower() == "" or " ":
            no_address = 'no address'
        else:
            no_address = form.address.data.lower()

        a = 'a b c 1 2 3 4 5 6 7 8 9 0 d e f g h i j k l m n o p q r s t u v w x y z'

        a = a.split(' ')
        b = []
        n = 0

        while n <= 32 :
            b.append(random.choice(a))
            n += 1

        code = ''.join(b)
        verify_email(form.email.data.lower(), code)
    
        braider = braiders(username=form.username.data.lower(),
                                        fullname=form.fullname.data.lower(),
                                        email=form.email.data.lower(),
                                        password=form.password1.data.lower(),
                                        token=code,
                                        phone_num=form.phone_num.data.lower(),
                                        country=form.country.data.lower(),
                                        city=form.city.data.lower(),
                                        address=no_address,
                                        instagram=form.instagram.data.lower(),
                                        website=form.website.data.lower(),
                                        twitter=form.twitter.data.lower(),
                                        youtube=form.youtube.data.lower(),
                                        )      

        db.session.add(braider)
        db.session.commit()

        # flash('your account has been created', category='success')

        return redirect(url_for('verify_page', email=form.email.data.lower()))


    if form.errors != {}:

        for err_msg in form.errors.values():

            if str(err_msg) == "['Field must be equal to password1.']":
                flash(f'Entered passwords was not the same. please try again.', category='danger')

            else:
                flash(f'There was an error: {err_msg}\n Please try again', category='danger')

    return render_template('register.html', form=form, sub_form=sub_form)


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():

    name = 'BRAIDSTARZ'
    loged_in = False
    true_user = False


    name, loged_in , true_user= authenticated(current_user, true_user, name)

    form = email_messages_form()
    sub_form = subscribe_form()

    if form.validate_on_submit():
        flash(f'Success! your message have been send dear {form.name.data}.', category='success')

        new_message = email_messages(name=form.name.data,
                                     email=form.email.data,
                                     message=form.message.data)

        db.session.add(new_message)
        db.session.commit()

        return render_template('contact.html', form=form, sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user)

    if sub_form.validate_on_submit():

        if subscribers.query.filter_by(email=sub_form.email.data).first():

            flash(f'The email {sub_form.email.data} has been subscribed. Please enter another email-address. ', category='danger')

        else:
            new_sub = subscribers(email=sub_form.email.data)
            db.session.add(new_sub)
            db.session.commit()

            flash('You subscribed successfuly!', category='success')

            return render_template('contact.html', form=form, sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user)

    return render_template('contact.html', form=form, sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user)


@app.route(f'/profile/<username>', methods=['GET', 'POST'])
def profile_page(username):

    true_user = False
    loged_in = False
    name = 'BRAIDSTARZ'

    name, loged_in , true_user= authenticated(current_user, true_user, name)

    sub_form = subscribe_form()
    subscribe(sub_form)

    info = braiders.query.filter_by(username=username).first_or_404()

    return render_template('profile.html', info=info, sub_form=sub_form, loged_in=loged_in, true_user=true_user, name=name)


@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile_page():

    edit_form = edit_braider_form()
    
    sub_form = subscribe_form()
    subscribe(sub_form)

    if edit_form.validate_on_submit():

        if edit_form.username.data == '':
            pass
        else:
            current_user.username = edit_form.username.data.lower()

        if edit_form.fullname.data == '':
            pass
        else:
            current_user.fullname = edit_form.fullname.data.lower()

        if edit_form.email.data == '':
            pass
        else:
            current_user.email = edit_form.city.data.lower()

        if edit_form.phone_num.data == '':
            pass
        else:
            current_user.phone_num = edit_form.phone_num.data.lower()

        if edit_form.country.data == '':
            pass
        else:
            current_user.country = edit_form.country.data.lower()

        if edit_form.city.data == '':
            pass
        else:
            current_user.city = edit_form.city.data.lower()

        if edit_form.instagram.data == '':
            pass
        else:
            current_user.instagram = edit_form.instagram.data.lower()

        if edit_form.twitter.data == '':
            pass
        else:
            current_user.twitter = edit_form.twitter.data.lower()

        if edit_form.youtube.data == '':
            pass
        else:
            current_user.youtube = edit_form.youtube.data.lower()

        if edit_form.website.data == '':
            pass
        else:
            current_user.website = edit_form.website.data.lower()

        db.session.commit()

        return redirect(url_for('profile_page', username=str(current_user.username)))

    return render_template('edit-profile.html', edit_form=edit_form, sub_form=sub_form)


@app.route('/nft', methods=['GET', 'POST'])
def nft_page():

    name = 'BRAIDSTARZ'
    loged_in = False
    true_user = False

    name, loged_in , true_user= authenticated(current_user, true_user, name)

    sub_form = subscribe_form()
    subscribe(sub_form)

    return render_template('NFT.html', sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user)


@app.route('/youtube', methods=['GET', 'POST'])
def youtube_page():

    name = 'BRAIDSTARZ'
    loged_in = False
    true_user = False

    name, loged_in , true_user= authenticated(current_user, true_user, name)

    sub_form = subscribe_form()
    subscribe(sub_form)

    return render_template('youtube.html', sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user)


@app.route('/edit-profile')
def main_route():

    if current_user.is_authenticated:
         return redirect(url_for('about_page'))
    else:
         return redirect(url_for('home_page'))


@app.route('/logout')
def logout_page():

    logout_user()
    flash('you have been logged out', category='info')
    return redirect(url_for('home_page'))


@app.route('/collection', methods=['GET', 'POST'])
def collection_page():

    name = 'BRAIDSTARZ'
    loged_in = False
    true_user = False

    images = []

    while i <= 78:

        images.append(f'normal-design ({i})')

        i = i + 1

    name, loged_in, true_user = authenticated(current_user, true_user, name)

    sub_form = subscribe_form()
    subscribe(sub_form)

    return render_template('collection.html', sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user, images=images)


@app.route('/collection-filter', methods=['GET', 'POST'])
def collection_filter_page():

    name = 'BRAIDSTARZ'

    loged_in = False
    true_user = False

    sub_form = subscribe_form()
    subscribe(sub_form)

    name, loged_in, true_user = authenticated(current_user, true_user, name)

    filter_form = collection_filter_form()

    return render_template('collection-filter.html', sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user, filter_form=filter_form)

@app.route('/verify/<email>')
def verify_page(email):

    name = 'BRAIDSTARZ'
    loged_in = False
    true_user = False
    sub_form = subscribe_form()
    subscribe(sub_form)
    name, loged_in, true_user = authenticated(current_user, true_user, name)  

    return render_template('verify.html', sub_form=sub_form, name=name, loged_in=loged_in, true_user=true_user, email=email)



def subscribe(sub_form):


    if sub_form.validate_on_submit():

        if subscribers.query.filter_by(email=sub_form.sub_email.data).first():

            flash(f'The email {sub_form.sub_email.data} has been subscribed. Please enter another email-address. ',
                  category='danger')

        else:
            new_sub = subscribers(email=sub_form.sub_email.data)
            db.session.add(new_sub)
            db.session.commit()

            flash('You subscribed successfully!', category='success')

    return sub_form

def authenticated(current_user, true_user, name):

    loged_in = False
    name = 'BRAIDSTARZ'

    if current_user.is_authenticated:

        name = current_user.username
        loged_in  = True

        if current_user.username == username:
            true_user = True

    return name, loged_in, true_user


