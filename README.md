# Data Engineering Project: Computer Science Students Analysis

This project analyzes computer science student data through a comprehensive data engineering pipeline.

## Week 1: Data Management and SQL Database Setup

### Prerequisites

- Microsoft SQL Server
- SQL Server Management Studio
- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
   ````
   git clone https://github.com/MahmoudMahdy448/cs-students-career-prediction.git
   cd <project-directory>
   ```

2. Install required Python packages:
   ````
   pip install -r requirements.txt
   ```

3. Configure the database connection:
   - Copy the `.env.example` file to `.env`
   - Edit `.env` with your SQL Server credentials

4. Create the database schema:
   - Open SQL Server Management Studio
   - Connect to your SQL Server instance
   - Open the `src/database/create_schema.sql` file
   - Execute the SQL script to create the necessary tables

5. Prepare the data:
   - Place the `cs_students.csv` file in the `data/raw/` directory

6. Run the ETL process:
   ````
   python src/etl/etl_process.py
   ```

### Verifying the Setup

1. Connect to your SQL Server instance
2. Query the `cs_students` table to ensure data has been loaded:
   ```sql
   SELECT TOP 10 * FROM cs_students;
   ```

3. Run basic analysis queries (examples in `src/database/analysis_queries.sql`)

## Project Structure

