from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()

def __repr__(self) -> str:
    return f"{self.sno}: {self.fname} {self.lname}"

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        todo=Todo(fname=fname,lname=lname)
        
        db.session.add(todo)
        db.session.commit()
    all_todo=Todo.query.all()
    return render_template('index.html',all_todo=all_todo)

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
