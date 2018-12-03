# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mgmtapp.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)

class CollectionDetails(db.Model):
    """"""
    __tablename__ = "details"

    id = db.Column(db.Integer, primary_key=True)

    project_name = db.Column(db.String)
    collection_type = db.Column(db.String)
    project_date = db.Column(db.String)

    begin_date = db.Column(db.String)
    begin_time = db.Column(db.String)
    designator = db.Column(db.String)
    loc_common = db.Column(db.String)
    loc_region = db.Column(db.String)
    loc_detailed = db.Column(db.String)
    collect_common = db.Column(db.String)
    altitude = db.Column(db.String)
    signal_type = db.Column(db.String)
    architecture = db.Column(db.String)
    band_no = db.Column(db.String)
    freq_bands = db.Column(db.String)
    antenna_loc = db.Column(db.String)

#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mgmtapp.db'
# app.secret_key = "flask rocks!"
#
# db = SQLAlchemy(app)