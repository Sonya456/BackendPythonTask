from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    description = request.json['description']
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)


@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    return tasks_schema.jsonify(all_tasks)


@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)


@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    title = request.json['title']
    description = request.json['description']
    task.title = title
    task.description = description
    db.session.commit()
    return task_schema.jsonify(task)


@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


