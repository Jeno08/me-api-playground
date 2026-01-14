-- SQLite Profile Database for Me-API Playground

CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    education TEXT,
    skills TEXT,        
    projects TEXT,      
    work_links TEXT     
);


CREATE INDEX IF NOT EXISTS idx_profile_skills ON profile(skills);
CREATE INDEX IF NOT EXISTS idx_profile_projects ON profile(projects);
