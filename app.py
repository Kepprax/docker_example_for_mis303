from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import art
import os

app = Flask(__name__)

# Veritabanı bağlantı ayarı
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:pass@db:5432/aybu_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    art.tprint("AYBU LOGIN", font="small") 
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    s_id = data.get('student_id')
    pwd = data.get('password')
    
    user = User.query.filter_by(student_id=s_id, password=pwd).first()
    
    if user:
        return jsonify({"status": "success", "message": f"Login Successful! Hello {s_id}"})
    return jsonify({"status": "error", "message": "Invalid Student ID or Password!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)