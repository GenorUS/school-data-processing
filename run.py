import argparse
from app import Slack, mysql_session, load_private_school, load_public_school_all, load_public_school_base, \
    load_public_school_membership, load_public_school_characteristics, load_public_school_eligibility, \
    load_public_school_staff, process_base_school_def, load_college_all, process_base_college_all
from config import SLACK_WEBHOOK, DB_DEV, DB_PROD
import os

process_ls = [
    'db-build',
    'db-load-private-all',
    # 'db-load-public-directory',
    # 'db-load-public-membership',
    # 'db-load-public-staff',
    # 'db-load-public-characteristics',
    # 'db-load-public-eligibility',
    'db-load-public-all',
    'db-load-college-all',
    'db-process-base-school-all',
    'db-process-base-college-all'
]

def get_file_path(filename):
    dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_files')
    return os.path.join(dir_path, filename)


def process_router(db_vals, process, slack, filename=None):

    default_files = {
        'private': get_file_path('private_all.csv'),
        'public_base': get_file_path('public_base.csv'),
        'public_mem': get_file_path('public_demo.csv'),
        'public_staff': get_file_path('public_staff.csv'),
        'public_char': get_file_path('public_characteristics.csv'),
        'public_elig': get_file_path('public_eligibility.csv'),
        'college_base': get_file_path('college_base.csv'),
        'college_academic_charges': get_file_path('college_academic_charges.csv'),
        'college_activity': get_file_path('college_activity.csv'),
        'college_enrollment': get_file_path('college_enrollment.csv'),
        'college_offering': get_file_path('college_offering.csv'),
        'college_program_charges': get_file_path('college_program_charges.csv'),
    }

    if process == 'db-build':
        slack.message('{} - building school data database'.format(db_vals['name'].upper()))
        mysql_session(db_vals)
        slack.message('{} - school data database build successful!'.format(db_vals['name'].upper()))

    elif process == 'db-load-private-all':
        slack.message('{} - loading private school data'.format(db_vals['name'].upper()))
        if filename:
            default_files['private'] = get_file_path(filename)
        session = mysql_session(db_vals)
        load_private_school(session, default_files)
        slack.message('{} - private school data load successful!'.format(db_vals['name'].upper()))

    elif process == 'db-load-public-all':
        slack.message('{} - loading public school data'.format(db_vals['name'].upper()))
        if filename:
            print('file overrides not supported for all')
        session = mysql_session(db_vals)
        load_public_school_all(session, default_files)
        slack.message('{} - public school data load successful'.format(db_vals['name'].upper()))

    # elif process == 'db-load-public-directory':
    #     if file_path:
    #         default_files['public_base'] = file_path
    #     session = mysql_session(db_vals)
    #     load_public_school_base(session, default_files)
    #
    # elif process == 'db-load-public-membership':
    #     if file_path:
    #         default_files['public_mem'] = file_path
    #     session = mysql_session(db_vals)
    #     load_public_school_membership(session, default_files)
    #
    # elif process == 'db-load-public-staff':
    #     if file_path:
    #         default_files['public_staff'] = file_path
    #     session = mysql_session(db_vals)
    #     load_public_school_staff(session, default_files)
    #
    # elif process == 'db-load-public-characteristics':
    #     if file_path:
    #         default_files['public_char'] = file_path
    #     session = mysql_session(db_vals)
    #     load_public_school_characteristics(session, default_files)
    #
    # elif process == 'db-load-public-eligibility':
    #     if file_path:
    #         default_files['public_elig'] = file_path
    #     session = mysql_session(db_vals)
    #     load_public_school_eligibility(session, default_files)

    elif process == 'db-load-college-all':
        slack.message('{} - loading college data'.format(db_vals['name'].upper()))
        if filename:
            print('file overrides not supported for all')
        try:
            session = mysql_session(db_vals)
            load_college_all(session, default_files)
            slack.message('{} - college data load successful'.format(db_vals['name'].upper()))
        except Exception as e:
            slack.message('{} - college data load unsuccessful: {}'.format(db_vals['name'].upper(), e))

    elif process == 'db-process-base-school-all':
        session = mysql_session(db_vals)
        process_base_school_def(session)

    elif process == 'db-process-base-college-all':
        session = mysql_session(db_vals)
        process_base_college_all(session)

    else:
        print("unknown process -- c'mon brah")


def get_db_vals(prod_flg):
    if prod_flg:
        return DB_PROD
    else:
        return DB_DEV


def run():

    prod_flg = False

    # slack client
    slack = Slack(SLACK_WEBHOOK, 'school-data')

    # define arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', metavar="e", nargs=1, help="environment, options: local, prod", required=True)
    parser.add_argument('-a', metavar="a", nargs=1, help="actions, options: {}".format("\n".join(process_ls)), required=True)
    parser.add_argument('-f', metavar="f", nargs='?', help="file in ./input_files")

    args = parser.parse_args()
    print(args.e)

    if args.e[0] == "prod":
        prod_flg = True

    action = args.a[0]

    if args.f:
        filename = args.f[0]
    else:
        filename = None

    db_vals = get_db_vals(prod_flg)

    process_router(db_vals, action, slack, filename=filename)


if __name__ == '__main__':
    run()