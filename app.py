from flask import Flask, render_template, request
from utils.transform import transform_spreadsheet
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path('import_data.db')


def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_number TEXT NOT NULL,
                department TEXT NOT NULL,
                email TEXT
            )
        ''')
        conn.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    records = []
    message = ''

    if request.method == 'POST':
        file = request.files.get('spreadsheet')
        if not file or not file.filename:
            message = 'Please select a CSV or Excel file.'
        else:
            try:
                records = transform_spreadsheet(file)
                with sqlite3.connect(DB) as conn:
                    for row in records:
                        conn.execute(
                            'INSERT INTO students (name, roll_number, department, email) VALUES (?, ?, ?, ?)',
                            (row['name'], row['roll_number'], row['department'], row['email'])
                        )
                    conn.commit()
                message = f'{len(records)} record(s) imported successfully.'
            except Exception as exc:
                message = f'Import failed: {exc}'

    return render_template('index.html', records=records, message=message)


@app.route('/records')
def records():
    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            'SELECT id, name, roll_number, department, email FROM students ORDER BY id DESC'
        ).fetchall()
    return render_template('records.html', records=rows)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
