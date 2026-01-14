# Me-API Playground - Melfin Jeno

Backend API: http://localhost:5000  
Frontend Demo: frontend/index.html  
Resume: [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/Jeno08)

# Architecture

# Features (All Working)
- `GET /health` → Server status
- `GET /profile` → Full resume data
- `GET /projects?skill=python` → Filter projects by skill
- `GET /skills/top` → Top 3 skills
- `GET /search?q=jeno` → Search profile

# Database Schema
```sql
CREATE TABLE profile (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),           -- "Melfin Jeno"
    email VARCHAR(100),          -- "dominer08@gmail.com"
    education TEXT,              -- "B.Tech AI/ML - Joy University, 4th Year"
    skills TEXT,                 -- "Python, Flask, SQL, Machine Learning, PyTorch, TensorFlow"
    projects TEXT,               -- "WhatsApp Chatbot using Python and Flask, NEET Tutor AI using ML models, Compiler Simulator in Python, Predictive Analytics with Python"
    work_links TEXT              -- "github.com/Jeno08, linkedin.com/in/yourprofile"
);

git clone https://github.com/Jeno08/me-api-playground.git
cd me-api-playground
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
python app.py

# Health check
curl http://localhost:5000/health

# Full profile
curl http://localhost:5000/profile

# Filter Python projects
curl http://localhost:5000/projects?skill=Python

# Top skills
curl http://localhost:5000/skills/top

Backend: Flask + Flask-SQLAlchemy + SQLite
Frontend: Vanilla HTML/CSS/JavaScript
Deployment: Render (backend) + Netlify (frontend)
Dev Tools: VS Code, Git, Python 3.10+

