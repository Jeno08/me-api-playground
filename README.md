# Me-API Playground - Melfin Jeno

<div align="center">
  <a href="https://spectacular-sprite-e59c82.netlify.app/">
    <img src="https://img.shields.io/badge/Frontend-LIVE-00C7B7?style=for-the-badge&logo=netlify&logoColor=white" alt="Frontend">
  </a>
  <a href="https://jeno-api.onrender.com/">
    <img src="https://img.shields.io/badge/Backend-LIVE-FAA63B?style=for-the-badge&logo=render&logoColor=white" alt="Backend">
  </a>
  <img src="https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge" alt="Status">
</div>

**Full-Stack Developer Portfolio API** - Live demo of REST API design, full-stack deployment, and modern frontend integration.

# Architecture

**Live URLs**

| Frontend | Backend API | Source Code |
|----------|-------------|-------------|
| [Try Demo](https://spectacular-sprite-e59c82.netlify.app/) | [API Base](https://jeno-api.onrender.com/) | [GitHub](https://github.com/Jeno08/me-api-playground) |

## **API Endpoints** (All Live!)

```bash
GET  https://jeno-api.onrender.com/health           # Server status
GET  https://jeno-api.onrender.com/profile          # Full resume data
GET  https://jeno-api.onrender.com/projects         # All projects
GET  https://jeno-api.onrender.com/projects?skill=python  # Filter projects
GET  https://jeno-api.onrender.com/skills/top       # Top 3 skills
GET  https://jeno-api.onrender.com/search?q=jeno    # Search profile


# Features
 5 RESTful endpoints with query parameters

 SQLite database with SQLAlchemy ORM

 Production deployment - Render (backend) + Netlify (frontend)

 CORS enabled frontend integration

 Real portfolio data - skills, projects, education

 Auto-deploy CI/CD from GitHub

 Modern UI - async fetch, error handling, glassmorphism



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

# Production Architecture
User → https://spectacular-sprite-e59c82.netlify.app/  (Netlify)
       ↓ JavaScript fetch()
API  → https://jeno-api.onrender.com/profile          (Render)
       ↓ SQLite DB
Data → Melfin Jeno's Portfolio

# Tech Stack

Backend:    Flask -  SQLAlchemy -  SQLite
Frontend:   HTML5 -  CSS3 -  Vanilla JS
Deployment: Netlify -  Render
Dev Tools:  VS Code -  Git -  GitHub

#Local setup

git clone https://github.com/Jeno08/me-api-playground.git
cd me-api-playground

# Backend
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
# → http://localhost:5000

# Frontend
# → Open frontend/index.html in browser


# Health check
curl https://jeno-api.onrender.com/health

# Full profile
curl https://jeno-api.onrender.com/profile

# Filter Python projects
curl "https://jeno-api.onrender.com/projects?skill=Python"

# Top skills
curl https://jeno-api.onrender.com/skills/top


# About

Melfin Jeno - B.Tech AI/ML (4th Year, Joy University)
Skills: Python • Flask • ML • APIs • Deployment
Projects: WhatsApp Chatbot • NEET Tutor AI • Compiler Simulator

<div align="center"> <a href="https://linkedin.com/in/melfinjeno"> <img src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"> </a> <a href="https://github.com/Jeno08"> <img src="https://img.shields.io/badge/GitHub-Follow-000?style=for-the-badge&logo=github&logoColor=white"> </a> </div>

License
MIT License - Free to use & modify!

<div align="center"> <strong> <a href="https://spectacular-sprite-e59c82.netlify.app/">Try Live Demo</a></strong> </div> ```