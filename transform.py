import pandas as pd

# Transform Map: source spreadsheet columns -> target database fields
TRANSFORM_MAP = {
    'Student Name': 'name',
    'Roll No': 'roll_number',
    'Department': 'department',
    'Email': 'email'
}


def transform_spreadsheet(file):
    filename = file.filename.lower()

    if filename.endswith('.csv'):
        data = pd.read_csv(file)
    elif filename.endswith('.xlsx'):
        data = pd.read_excel(file)
    else:
        raise ValueError('Only CSV and XLSX files are supported.')

    missing = [col for col in TRANSFORM_MAP if col not in data.columns]
    if missing:
        raise ValueError('Missing column(s): ' + ', '.join(missing))

    # Apply the Transform Map.
    data = data.rename(columns=TRANSFORM_MAP)
    data = data[['name', 'roll_number', 'department', 'email']].fillna('')
    return data.to_dict(orient='records')
