import os
from sqlalchemy import text


def jrnl_new_build(engine, schema, path, file_ls):
    for file in file_ls:
        filepath = os.path.join(path, file)
        fs = open(filepath, 'r').read()
        q = fs.format(schema)
        engine.execute(text(q))
        print('{} processed successfully'.format(file))


