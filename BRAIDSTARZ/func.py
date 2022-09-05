def find_braiders(db, by, table):

    result = db.session.query(table).filter(table.username.like(f'%{by.lower()}%'))

    if result.first():
        return result
    else:
        result = db.session.query(table).filter(table.city.like(f'%{by.lower()}%'))
        if result.first():
            return result
        else:
            result = db.session.query(table).filter(table.country.like(f'%{by.lower()}%'))
            if result.first():
                return result
            else:
                result = db.session.query(table).filter(table.fullname.like(f'%{by.lower()}%'))
                if result.first():
                    return result
                else:
                    result = db.session.query(table).filter(table.address.like(f'%{by.lower()}%'))
                    if result.first():
                        return result
                    else:
                        result = db.session.query(table).filter(table.instagram.like(f'%{by.lower()}%'))
                        if result.first():
                            return result
                        else:
                            result = db.session.query(table).filter(table.twitter.like(f'%{by.lower()}%'))
                            if result.first():
                                return result
                            else:
                                result = db.session.query(table).filter(table.youtube.like(f'%{by.lower()}%'))
                                if result.first():
                                    return result
                                else:
                                    result = False

    return result

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

