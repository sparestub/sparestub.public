"""
Routes and views for the flask application.
"""
import os

from datetime import datetime
from flask import render_template,redirect
from SpareStubPublic import app


@app.route('/')
def beta():
    """ redirect to sparestub with 302 (temporary redirect code) """
    return redirect("https://beta.sparestub.com", code=302)

#@app.route('/')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

@app.route('/original')
def original():
    """renders original"""
    return render_template(
        'original.html',
        title='Original',
        year=datetime.now().year,
        message='Your application description page.'
    )