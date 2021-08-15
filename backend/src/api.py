import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# test the route
@app.route('/')
def index():
    return 'Hello, coffee!'

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
# db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
# 
@app.route('/drinks', methods=['GET'], endpoint='get_drinks_short')
def get_drinks():
     
    try:
        drinks = Drink.query.all()
    except:
        abort(400)
    return jsonify({
        'success': True,
        'drinks': [drink.short() for drink in drinks]
    })

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
# 
@app.route('/drinks-detail', methods=['GET'], endpoint='get_drinks_long')
@requires_auth('get:drinks-detail')
def get_drinks_detail(jwt):
    
    try:
        drinks = Drink.query.all()
    except:
        abort(401)
    return jsonify({
        'success': True,
        'drinks': [drink.long() for drink in drinks]
    })

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'], endpoint='post_drinks')
@requires_auth('post:drinks')
def create_drinks(jwt):

    # The request should be in the format of:
    # data = dict(request.form or request.json or request.data)
    data = request.get_json()

    try:
        # title = data.get('title')
        title = data['title']

        # if type(data.get('recipe')) == str:
        #     recipe = data.get('recipe')
        # else:
        #     recipe = json.dumps(data.get('recipe'))
        recipe = json.dumps(data['recipe'])

    except:
        abort(400)

    if title == '' or recipe == '':
        abort(400)

    drink = Drink(title=title, recipe=recipe)
    drink.insert()

    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'], endpoint='patch_drinks')
@requires_auth('patch:drinks')
def update_drinks(jwt, id):

    drink = Drink.query.filter(Drink.id==id).one_or_none()

    if drink is None:
        abort(404)

    data = dict(request.form or request.json or request.data)
    try:
        title = data.get('title')

        if type(data.get('recipe')) == str:
            recipe = data.get('recipe')
        else:
            recipe = json.dumps(data.get('recipe'))

        if 'title' in data:
            drink.title = title
        if 'recipe' in data:
            drink.recipe = recipe

        drink.update()
    except:
        abort(400)
    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['DELETE'], endpoint='delete_drinks')
@requires_auth('delete:drinks')
def delete_drinks(jwt, id):

    drink = Drink.query.filter(Drink.id==id).one_or_none()
    if not drink:
        return (404)
    try:
        drink.delete()
    except:
        abort(400)
    return jsonify({
        'success': True,
        'delete': str(id)
    })

# Error Handling
'''
Example error handling for unprocessable entity
'''

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(400)
def bad_request(error):
        return jsonify({
          'success': False,
          'message': 'bad request',
          'error': 400
        }), 400
'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
@app.errorhandler(401)
def not_found(error):
        return jsonify({
          'success': False,
          'message': 'wrong crediential or unclear authorization',
          'error': 401
          }), 401

@app.errorhandler(403)
def not_found(error):
        return jsonify({
          'success': False,
          'message': 'not authorized',
          'error': 403
          }), 403

@app.errorhandler(405)
def not_allowed(error):
        return jsonify({
          'success': False,
          'message': 'method is not allowed',
          'error': 405
        }), 405

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found(error):
        return jsonify({
          'success': False,
          'message': 'not found',
          'error': 404
          }), 404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def auth_error(error):
    response = jsonify(error.error)
    response.status_code = error.status_code
    return response

