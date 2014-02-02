#! /usr/bin/env python

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.config.from_object('config')

# Default views

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static/img'),
    'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/humans.txt')
def humans():
  return render_template('humans.txt')

@app.route('/robots.txt')
def robots():
  return render_template('robots.txt')

@app.errorhandler(403)
def access_forbidden(e):
  return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500

# Controller logic

@app.route('/')
def index():
  return render_template('index.html')