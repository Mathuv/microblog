from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):

        '''The __repr__ method tells Python how to print objects of this class. 
        We will use this for debugging.'''

        return '<User %>' % self.nickname
