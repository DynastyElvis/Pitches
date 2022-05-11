from datetime import datetime#import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer # for generating tokens
from pitch import db, login_manager, app #importing the database and login manager
from flask_login import UserMixin #, current_user


@login_manager.user_loader #for loading the user
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin): #creating the user class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    pitches = db.relationship('Pitch', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    
    @staticmethod #for creating the user
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
            
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Pitch(db.Model): #creating the pitch class
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
    def __repr__(self):
        return f"Pitch('{self.title}', '{self.date_posted}')"
    
class Comment(db.Model): #creating the comment class
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userdata = db.Column(db.Text, nullable=False )
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'), nullable=True)
    
    
# class Like(db.Model):