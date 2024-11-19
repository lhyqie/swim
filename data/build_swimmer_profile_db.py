import csv
import os

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from data.schema import db, SwimmerProfile

main = Blueprint("main", __name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def build():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'swimmer-profile.db')
    app.register_blueprint(main)
    db.init_app(app)
    with app.app_context():
        db.drop_all()  # drop existing tables first
        db.create_all()
        load_data(csv_file="data/swimmer-profile-top1000-per-group.csv")
    return app


def load_data(csv_file):
    with open(csv_file) as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='|')
        for row in reader:
            sp = SwimmerProfile(id=row['id'], firstname=row['firstname'], lastname=row['lastname'], team=row['team'], age=int(row['age']))
            db.session.add(sp)
    db.session.commit()


if  __name__ == '__main__':
    port = 5000
    debug = True
    app = build()
    # app.run(debug=debug, port=port)
