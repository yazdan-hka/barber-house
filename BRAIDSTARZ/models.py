from BRAIDSTARZ import db, login_manager
from BRAIDSTARZ import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return braiders.query.get(user_id)


class braiders(db.Model, UserMixin):

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8 ')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    fullname = db.Column(db.String(length=40), nullable=False)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.String(length=15), nullable=True, unique=True)
    country = db.Column(db.String(length=30), nullable=False)
    city = db.Column(db.String(length=30), nullable=False)
    address = db.Column(db.String(length=512))
    website = db.Column(db.String(length=128))
    instagram = db.Column(db.String(length=30))
    youtube = db.Column(db.String(length=50))
    twitter = db.Column(db.String(length=30))


class email_messages(db.Model, UserMixin):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50))
    email = db.Column(db.String(length=80))
    message = db.Column(db.String(length=1024))


class subscribers(db.Model, UserMixin):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(length=100), unique=True, nullable=False)


class images(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    file_name = db.Column(db.String(64), unique=True)
    under_14 = db.Column(db.Boolean(), default=False, nullable=False)
    design = db.Column(db.Boolean(), default=False, nullable=False)
    box = db.Column(db.Boolean(), default=False, nullable=False)
    dutch_french = db.Column(db.Boolean(), default=False, nullable=False)
    goddes = db.Column(db.Boolean(), default=False, nullable=False)
    crochet = db.Column(db.Boolean(), default=False, nullable=False)
    cornrows = db.Column(db.Boolean(), default=False, nullable=False)
    stitch = db.Column(db.Boolean(), default=False, nullable=False)
    special = db.Column(db.Boolean(), default=False, nullable=False)  
    trend = db.Column(db.Boolean(), default=False, nullable=False)   



    id = db.Column(db.Integer, primary_key=True)
    can_view_records = db.Column(db.Boolean, default=False, nullable=False)




















# (fullname='', username='', email='', password_hash='', phone_num='' country='', city='', address='', instagram='', youtube='', twitter='')
# y = braiders(fullname='omid shirali', username='omid_id', email='omid@gmail.com', password_hash='hrgrj46uy5grbgnhjuy', phone_num='093xxxxx146', country='iran', city='tehran', address='tajrish, dezashib', instagram='omidshirali', youtube='idonno', twitter='twiwis')
"""username, password, email, phone_num, Country, City, Address, fullname, instagram, twitter, youtube
"""
