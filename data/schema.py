from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SwimmerProfile(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=True)

    def __lt__(self, other: 'SwimmerProfile') -> bool:
        if self.id != other.id:
            return self.id < other.id
        if self.team != other.team:
            return self.team < other.team
        if self.firstname != other.firstname:
            return self.firstname < other.firstname
        return self.lastname < other.lastname
