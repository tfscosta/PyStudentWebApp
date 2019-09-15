from flask import request, render_template, make_response, jsonify, Response, abort
from datetime import datetime as dt
from flask import current_app as app
from flask_restful import Api


# GET /students
# @app.route('/students')
# def get_students():
#     students = Student.query.all()
#     return Response(jsonify(students), mimetype='application/json')

# # Get student/{id}
# @app.route('/students/<int:student_number>')
# def get_student(student_number):
#     student = Student.query.filter_by(id=student_number).first()
#     if student is None:
#         return abort(404)
#     else:
#         return Response(jsonify(student), mimetype='application/json')


@app.errorhandler(400)
def bad_request(error):
    """
    Gives error message when any bad requests are made.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    """
    Gives error message when any invalid url are requested.
    Args:
        error (string): 
    Returns:
        Error message.
    """
    print(error)
    return make_response(jsonify({'error': 'Not found'}), 404)
