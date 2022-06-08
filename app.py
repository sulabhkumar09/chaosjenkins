# import main Flask class and request object
from flask import Flask, request, jsonify
from pdchaos.middleware.contrib.flask.flask_middleware import FlaskMiddleware


# create the Flask app
app = Flask(__name__)
app.config['CHAOS_MIDDLEWARE_APPLICATION_NAME'] = 'chaos-toolkit-for-webapp'
app.config['CHAOS_MIDDLEWARE_APPLICATION_ENV'] = 'chaos-toolkit-for-webapp-environment'
app.config['CHAOS_MIDDLEWARE_PROOFDOCK_API_TOKEN'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

middleware = FlaskMiddleware(app)

@app.route('/')
def status_check():
    return 'Website is ok'

@app.route('/return-failure')
def return_failure():
    return 'Return a failure response'

@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return jsonify({"name": "Karan"}), 200

if __name__ == '__main__':
    # run app in debug mode on port 5002
    app.run(host='0.0.0.0', debug=True, port=5002)