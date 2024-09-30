-- Create the cs_students table
CREATE TABLE cs_students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    gpa DECIMAL(3,2),
    major VARCHAR(50),
    interested_domain VARCHAR(100),
    projects VARCHAR(255),
    future_career VARCHAR(100),
    python_skill VARCHAR(20),
    sql_skill VARCHAR(20),
    java_skill VARCHAR(20)
);