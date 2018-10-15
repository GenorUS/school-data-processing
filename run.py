import argparse
from app import Slack, mysql_engine, jrnl_new_build
from config import SLACK_WEBHOOK, DB_DEV, DB_PROD, NEW_BUILD_SCRIPTS
import os


slack = Slack(SLACK_WEBHOOK, 'school-data')


def process_router(engine, schema, process):
    if process == 'jrnl-new-build':
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sql_build_scripts')
        jrnl_new_build(engine, schema, dir_path, NEW_BUILD_SCRIPTS)
    elif process == 'jrnl-process-all':
        print(process)
    elif process == 'jrnl-public-base':
        print(process)
    elif process == 'jrnl-public-demographics':
        print(process)
    elif process == 'jrnl-public-eligibility':
        print(process)
    elif process == 'jrnl-public-characteristics':
        print(process)
    elif process == 'jrnl-public-staff':
        print(process)
    elif process == 'jrnl-private-all':
        print(process)
    else:
        print('unknown process')


parser = argparse.ArgumentParser()
parser.add_argument("environment", type=str, help="environment, options: local, prod")
parser.add_argument("process", type=str, help="processes, options: {}".format("\n".join(NEW_BUILD_SCRIPTS)))
# parser.add_argument("filename", type=str, help="processing file")

args = parser.parse_args()

if args.environment == "local":
    engine = mysql_engine(DB_DEV)
    db_schema = DB_DEV['schema']
    process_router(engine, db_schema, args.process)
#
#
#         q = "describe genorus_school_data.jrnl_public_school_def"
#         res = engine.execute(q).fetchall()
#         for i in res:
#             print(i)
#         # slack.message("Processing {}".format(args.filename))
#     else:
#         print("unknown process")
# elif args.environment == "prod":
#     if args.process in process_ls:
#         print("shouldn't be here")
#         # slack.message("Processing {}".format(args.filename))
#     else:
#         print("unknown process")
# else:
#     print("unknown environment")








# slack = Slack(SLACK_WEBHOOK, 'school-data')
# slack.message("testing")
