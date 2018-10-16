import os
from sqlalchemy import text

from datetime import datetime
from ..models import JrnlPrivateSchool


# def jrnl_new_build(): # engine, schema, path, file_ls
#     print('here')
#     # for file in file_ls:
#     #     filepath = os.path.join(path, file)
#     #     fs = open(filepath, 'r').read()
#     #     q = fs.format(schema)
#     #     engine.execute(text(q))
#     #     print('{} processed successfully'.format(file))
#     JrnlPrivateSchool.create()
#
# def jrnl_load_public_base(engine, schema, path, file_nm):
#     filepath = os.path.join(path, file_nm)
#     with open(filepath, newline='') as input_file:
#         reader = csv.DictReader(input_file, delimiter=",")
#         print(list(reader))
#
# def jrnl_load_private_all(engine, schema, path, file_nm):
#     filepath = os.path.join(path, file_nm)
#     # table_nm = 'jrnl_private_school_def'
#     # wipe_existing(engine, schema, table_nm)
#     output = []
#     with open(filepath, newline='') as input_file:
#         reader = csv.DictReader(input_file, delimiter=",")
#         counter = 0
#         for row in reader:
#             counter += 1
#             row['UPDATED_TS'] = datetime.now()
#             row['INSERTED_TS'] = datetime.now()
#
#             if counter % 1000 == 0:
#                 print("{} records processed".format(counter))
#         print('records successfully inserted')
#
