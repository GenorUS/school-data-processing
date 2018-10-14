import argparse
from app import Slack
from config import SLACK_WEBHOOK

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
parser.add_argument("process", type=str, help="processes, options: {}".format("\n".join(process_ls)))
parser.add_argument("filename", type=str, help="processing file")

args = parser.parse_args()

if args.process in process_ls:
    slack.message("Processing {}".format(args.filename))
else:
    print("unknown process")


# slack = Slack(SLACK_WEBHOOK, 'school-data')
# slack.message("testing")
