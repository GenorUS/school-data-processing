import argparse
from app import Slack, mysql_engine, mysql_session
from config import SLACK_WEBHOOK, DB_DEV, DB_PROD


process_ls = [
    'jrnl-public-base',
    'jrnl-public-demographics',
    'jrnl-public-eligibility',
    'jrnl-public-characteristics',
    'jrnl-public-staff',
    'jrnl-private-all'
]

slack = Slack(SLACK_WEBHOOK, 'school-data')

parser = argparse.ArgumentParser()
parser.add_argument("environment", type=str, help="environment, options: local, prod")
parser.add_argument("process", type=str, help="processes, options: {}".format("\n".join(process_ls)))
parser.add_argument("filename", type=str, help="processing file")

args = parser.parse_args()

if args.environment == "local":
    if args.process in process_ls:
        engine = mysql_engine(DB_DEV)
        q = "describe genorus_school_data.jrnl_public_school_def"
        res = engine.execute(q).fetchall()
        for i in res:
            print(i)
        # slack.message("Processing {}".format(args.filename))
    else:
        print("unknown process")
elif args.environment == "prod":
    if args.process in process_ls:
        print("shouldn't be here")
        # slack.message("Processing {}".format(args.filename))
    else:
        print("unknown process")
else:
    print("unknown environment")



# slack = Slack(SLACK_WEBHOOK, 'school-data')
# slack.message("testing")
