# Import Data using Transform Maps (Spreadsheet)

## Project Description
This project demonstrates **Import Data using Transform Maps** with a simple Flask web application.
A CSV or Excel spreadsheet is uploaded, its source columns are mapped to target database fields, and the transformed records are stored in SQLite.

## Transform Map

| Spreadsheet Column | Target Field |
|---|---|
| Student Name | name |
| Roll No | roll_number |
| Department | department |
| Email | email |

## Features
- Upload CSV or XLSX spreadsheet
- Transform source columns to target fields
- Display imported data
- Store records in SQLite database
- View all imported records

## How to Run
1. Install Python 3.
2. Open terminal in this project folder.
3. Run `pip install -r requirements.txt`.
4. Run `python app.py`.
5. Open the Flask address shown in the terminal.
6. Upload `dataset/student_data.xlsx` or `dataset/student_data.csv`.
7. Click **Import & Transform**.

## Project Structure
- `app.py` - Flask application
- `utils/transform.py` - Transform Map and spreadsheet processing
- `templates/` - HTML pages
- `static/style.css` - CSS styling
- `dataset/` - Sample spreadsheet files
- `requirements.txt` - Python packages
- `README.md` - Project documentation
