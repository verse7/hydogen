import os
import jwt
from functools import wraps
from flask import render_template, request, jsonify
from server import app, db, csrf
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash

###
# Utility functions
###


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth:
            return jsonify({'code': 'authorization_header_missing', 
                            'description': 'Authorization header is expected'}), 401

        parts = auth.split()

        if parts[0].lower() != 'bearer':
            return jsonify({'code': 'invalid_header', 
                            'description': 'Authorization header must start with Bearer'}), 401
        elif len(parts) == 1:
            return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
        elif len(parts) > 2:
            return jsonify({'code': 'invalid_header', 
                            'description': 'Authorization header must be Bearer + \s + token'}), 401

        token = parts[1]
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except jwt.ExpiredSignature:
            return jsonify({'code': 'token_expired', 
                            'description': 'token is expired'}), 401
        except jwt.DecodeError:
            return jsonify({'code': 'token_invalid_signature', 
                            'description': 'Token signature is invalid'}), 401

        return f(*args, **kwargs)

    return decorated


def form_errors(form):
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages


###
# API endpoints
###


@app.route('/api/auth/register', methods=['POST'])
def register():
    pass

@app.route('/api/auth/login', methods=['POST'])
def login():
    pass

@app.route('/api/auth/logout', methods=['POST'])
@auth_required
def logout():
    pass

###
# This route yields control to vue
###
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

###
# The functions below should be applicable to all Flask apps.
###

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

