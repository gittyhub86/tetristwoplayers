from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/multiplayer')
def multiplayer():
    """Return a friendly HTTP greeting."""
    return render_template('multiplayer.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404