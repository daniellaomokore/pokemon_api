import json

from flask import Flask, jsonify, request, make_response#

from Pokemon import pokemon

app = Flask(__name__)

""" STATUS CODE ERROR HANDLING """
@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'error' : 'Not Found - Requested resource not found'}), 404)

@app.errorhandler(405)
def handle_405_error(_error):
    return make_response(jsonify({'error' : 'This method is not allowed for the request URL'}), 405)

@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({'error': 'Internal server error occurred'}), 500)

@app.errorhandler(401)
def handle_401_error(_error):
    return make_response(jsonify({'error': 'Unauthorised'}), 401)




""" GETTING INFORMATION FROM THE API """
""" This can be done directly from the browser """

# GET request - As an API, info is retrieved from the API URL as requested by client/user.

# @app.route() should contain the URL the app exists under and it's HTTP method
@app.route('/', methods=['GET'])
def hello():
    return {'hello': 'Universe'}



@app.route('/post', methods=['POST'])
def helloo():
    string = {'Names:': pokemon['name']}
    return string


if __name__ == '__main__':                     #if this(current file name) is the program that i'm actually running
    app.run(debug=True)                        #then run this
