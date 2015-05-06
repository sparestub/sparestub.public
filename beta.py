import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def start():
    """ redirect to sparestub with 302 (temporary redirect code) """
    return redirect("https://beta.sparestub.com", code=302)
