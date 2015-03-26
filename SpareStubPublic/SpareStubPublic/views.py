"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from SpareStubPublic import app

@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/original')
def original():
    """renders original"""
    return render_template(
        'original.html',
        title='Original',
        year=datetime.now().year,
        message='Your application description page.'
    )