import csv
from datetime import datetime


def csv_to_dicts(file_path, include_ts=True):
    output = []
    with open(file_path, newline='') as input_file:
        reader = csv.DictReader(input_file, delimiter=",")
        counter = 0
        for row in reader:
            record = {}
            counter += 1
            for key, val in row.items():
                upper_key = key.upper()
                record[upper_key] = val
                if include_ts:
                    record['UPDATED_TS'] = datetime.now()
                    record['INSERTED_TS'] = datetime.now()
            output.append(record)
            if counter % 2000 == 0:
                print('{} records processed'.format(counter))
    print('{} records from {}'.format(counter, file_path))
    return output
