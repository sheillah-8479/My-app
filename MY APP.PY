from flask import Flask, request, render_template, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract
from datetime import datetime
import calendar
import re

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
    submission_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)

def generate_slug(name):
    return re.sub(r'\W+', '-', name.lower())

@app.route('/')
def index():
    return render_template('obituary_form.html')

@app.route('/submit_obituary', methods=['POST'])
def submit_obituary():
    name = request.form['name']
    date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
    date_of_death = datetime.strptime(request.form['date_of_death'], '%Y-%m-%d').date()
    content = request.form['content']
    author = request.form['author']
    slug = generate_slug(name)

    new_obituary = Obituary(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death, content=content, author=author, slug=slug)

    try:
        db.session.add(new_obituary)
        db.session.commit()
        return "Obituary submitted successfully!"
    except Exception as e:
        db.session.rollback()
        return f"An error occurred: {str(e)}"

@app.route('/view_obituaries', methods=['GET'])
def view_obituaries():
    search_query = request.args.get('search', '')

    obituaries = Obituary.query

    if search_query:
        search_query = f"%{search_query}%"
        obituaries = obituaries.filter(
            Obituary.name.ilike(search_query) |
            Obituary.date_of_birth.ilike(search_query) |
            Obituary.date_of_death.ilike(search_query)
        )

    obituaries = obituaries.all()

    return render_template('view_obituaries.html', obituaries=obituaries)

@app.route('/edit_obituary/<int:obituary_id>', methods=['GET', 'POST'])
def edit_obituary(obituary_id):
    obituary = Obituary.query.get_or_404(obituary_id)

    if request.method == 'POST':
        obituary.name = request.form['name']
        obituary.date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()
        obituary.date_of_death = datetime.strptime(request.form['date_of_death'], '%Y-%m-%d').date()
        obituary.content = request.form['content']
        obituary.author = request.form['author']

        try:
            db.session.commit()
            return redirect(url_for('view_obituaries'))
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {str(e)}"

    return render_template('edit_obituary.html', obituary=obituary)

@app.route('/sitemap.xml')
def sitemap():
    pages = []
    obituaries = Obituary.query.all()

    for obituary in obituaries:
        url = url_for('view_obituaries', _external=True)
        lastmod = obituary.submission_date.strftime('%Y-%m-%d')
        pages.append({
            'loc': url,
            'lastmod': lastmod,
            'changefreq': 'monthly',
            'priority': '0.8'
        })

    xml_sitemap = render_template('sitemap_template.xml', pages=pages)
    response = Response(xml_sitemap, mimetype='application/xml')
    return response

if __name__ == '__main__':
    app.run(debug=True)
