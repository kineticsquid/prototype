import os
import sys
from flask import Flask, send_file


app = Flask(__name__)

@app.route('/')
def home():
    return send_file('static/ee-index.html')

@app.route('/connect')
def connect():
    return send_file('static/ee-stay-connected.html')

@app.route('/connect/')
def connect2():
    return send_file('static/ee-stay-connected.html')

@app.route('/badges')
def badges():
    return send_file('static/badges.html')

@app.route('/credly')
def credly():
    return send_file('static/credly.html')

@app.route('/jakarta-developer')
def jakarta_developer():
    return send_file('static/jakarta-developer.html')

@app.route('/jakarta-application-developer')
def jakarta_application_developer():
    return send_file('static/jakarta-application-developer.html')

@app.route('/class/jakarta-application-developer')
def jakarta_application_developer_class():
    return send_file('static/jakarta-application-developer-class.html')

@app.route('/class/jakarta-developer')
def jakarta_developer_class():
    return send_file('static/jakarta-developer-class.html')

@app.route('/test/jakarta-application-developer')
def jakarta_application_developer_test():
    return send_file('static/jakarta-application-developer-test.html')

@app.route('/test/jakarta-developer')
def jakarta_developer_test():
    return send_file('static/jakarta-developer-test.html')

@app.route('/style/<path:path>')
def style(path):
    return send_file('static/stylesheets/%s' % path)

@app.route('/css/<path:path>')
def css(path):
    return send_file('static/css/%s' % path)

@app.route('/images/<path:path>')
def image(path):
    return send_file('static/images/%s' % path)

@app.route('/fonts/<path:path>')
def font(path):
    return send_file('static/fonts/%s' % path)

@app.route('/js/<path:path>')
def js(path):
    return send_file('static/js/%s' % path)

@app.route('/build', methods=['GET', 'POST'])
def build():
    return date_environ

print('Starting %s....' % sys.argv[0])
print('Python: ' + sys.version)
date_environ = os.environ.get('DATE')
if date_environ is None:
    date_environ = 'dev environment'
print('Running build: %s' % date_environ)
print('Environment Variables:')
environment_vars = dict(os.environ)
print(environment_vars)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))