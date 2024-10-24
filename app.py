from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()

def __repr__(self) -> str:
    return f"{self.sno}: {self.name}"

@app.route('/')
def hello_world():
    todo=Todo(name="Nikita")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

@app.route('/show')
def show():
    all_todo=Todo.query.all()
    return render_template('index.html',all_todo=all_todo)

def create_database():
    with app.app_context():
        db.create_all()  # This creates the tables

if __name__ == "__main__":
 # Create the database tables
    app.run(debug=True)  # Then start the app
