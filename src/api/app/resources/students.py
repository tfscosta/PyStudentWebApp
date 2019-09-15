from flask_restful import Resource, abort, request
from ..Model import Student as StudentRepository
from marshmallow import ValidationError


class StudentsResource(Resource):
    schema = StudentRepository.StudentSchema()
    repository = StudentRepository.Student()

    def get(self):
        students = self.repository.query.all()
        return self.schema.dump(students, many=True)

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = self.schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        new_student = StudentRepository.Student()
        new_student.name = data["name"]
        new_student.commit()
        return {}, 201


class StudentResource(Resource):
    schema = StudentRepository.StudentSchema()
    repository = StudentRepository.Student()

    def get(self, id):
        student = self.repository.query.filter_by(id=id).first()
        if student is None:
            # Not found so HTTP 404 code
            abort(404, errorMessage="Student {} not found".format(id), code=404)
        return student

    def put(self, id):
        json_data = request.get_json()

        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = self.schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422

        student = StudentRepository.Student()
        student.name = data["name"]
        student.id = id
        student.commit()

        return self.schema.dump(student)

    def delete(self, id):

        student = StudentRepository.Student()
        student.id = id

        if student.delete():
            return {}, 200
        else:
            abort(404, errorMessage="Student {} not found".format(id), code=404)
