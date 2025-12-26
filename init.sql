CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    student_id VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

INSERT INTO users (student_id, password) VALUES 
('210101001', 'aybu123'),
('210101002', 'sifre456'),
('admin', 'admin123');