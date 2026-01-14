from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profile.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    education = db.Column(db.Text)
    skills = db.Column(db.Text)
    projects = db.Column(db.Text)
    work_links = db.Column(db.Text)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'education': self.education,
            'skills': self.skills.split(', ') if self.skills else [],
            'projects': self.projects.split('|||') if self.projects else [],
            'work_links': self.work_links.split(', ') if self.work_links else []
        }

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/profile', methods=['GET'])
def profile():
    p = Profile.query.first()
    return jsonify(p.to_dict()) if p else jsonify({'error': 'No profile yet'})

@app.route('/projects', methods=['GET'])
def get_projects():
    skill = request.args.get('skill', '').lower()
    p = Profile.query.first()
    if not p or not p.projects: 
        return jsonify([])
    
    projects = p.projects.split('|||')
    if skill:
        projects = [proj for proj in projects if skill in proj.lower()]
    return jsonify(projects)

@app.route('/skills/top', methods=['GET'])
def top_skills():
    p = Profile.query.first()
    if not p: 
        return jsonify([])
    skills = p.skills.split(', ')
    return jsonify({'top_skills': skills[:3]})

@app.route('/search', methods=['GET'])
def search():
    q = request.args.get('q', '').lower()
    p = Profile.query.first()
    if not p: 
        return jsonify([])
    
    results = []
    if q in (p.name or '').lower() or q in (p.education or '').lower():
        results.append({'type': 'profile', 'name': p.name})
    return jsonify(results)

def seed_data():
    if Profile.query.first():
        return
    p = Profile(
        name="Melfin Jeno", 
        email="dominer08@gmail.com",  
        education="B.Tech AI/ML - Joy University, 4th Year",
        skills="Python, Flask, SQL, Machine Learning, PyTorch, TensorFlow",
        projects="WhatsApp Chatbot|||NEET Tutor AI|||Compiler Simulator|||Predictive Analytics",
        work_links="github.com/Jeno08, linkedin.com/in/yourprofile"
    )
    db.session.add(p)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(host='127.0.0.1', port=5000, debug=True)
