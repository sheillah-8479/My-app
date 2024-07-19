from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///obituary_platform.db'
db = SQLAlchemy(app)

class Obituary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_death = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    submission_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'<Obituary {self.id}: {self.name}>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database and tables created successfully.")
    app.run(debug=True)
