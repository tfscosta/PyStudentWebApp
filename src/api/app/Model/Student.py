from .. import db, ma
import json


class Student(db.Model):

    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def commit(self):
        result = Student.query.filter_by(id=self.id)
        if result.count() == 0:
            db.session.add(self)
        else:
            student_to_update = result.first()
            student_to_update.name = self.name

        db.session.commit()

    def delete(self):
        result = Student.query.filter_by(id=self.id)
        if result.count() == 0:
            return False
        result.delete()
        db.session.commit()
        return True


class StudentSchema(ma.Schema):
    class Meta:
            # Fields to expose
        fields = ("id", "name")
