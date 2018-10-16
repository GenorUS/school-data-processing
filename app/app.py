from .models import mysql_session, JrnlPrivateSchool, JrnlPublicSchoolBase, JrnlPublicSchoolStaff, \
    JrnlPublicSchoolMembership, JrnlPublicSchoolEligibility, JrnlPublicSchoolCharacteristics
from .processing import csv_to_dicts


def create_session(db_dict):
    mysql_session(db_dict)


def load_private_school(session, input_dict):
    input_file = input_dict['private']
    data = csv_to_dicts(input_file)
    print(data[0])
    print("not implemented")


def load_public_school_base(session, input_dict):
    input_file = input_dict['public_base']
    data = csv_to_dicts(input_file)
    print(data[0])
    print("not implemented")


def load_public_school_membership(session, input_dict):
    input_file = input_dict['public_mem']
    data = csv_to_dicts(input_file)
    print(data[0])
    print("not implemented")


def load_public_school_staff(session, input_dict):
    input_file = input_dict['public_staff']
    data = csv_to_dicts(input_file)
    print(data[0])
    print("not implemented")


def load_public_school_characteristics(session, input_dict):
    input_file = input_dict['public_char']
    data = csv_to_dicts(input_file)
    print(data[0])
    print("not implemented")


def load_public_school_eligibility(session, input_dict):
    input_file = input_dict['public_elig']
    data = csv_to_dicts(input_file)
    print(data[0])
    print("not implemented")


def load_public_school_all(session, input_dict):
    print("loading public_school_base")
    load_public_school_base(session, input_dict)
    print("done!")
    print("loading public_school_membership")
    load_public_school_membership(session, input_dict)
    print("done!")
    print("loading public_school_staff")
    load_public_school_staff(session, input_dict)
    print("done!")
    print("loading public_school_characteristics")
    load_public_school_characteristics(session, input_dict)
    print("done!")
    print("loading public_school_eligibility")
    load_public_school_eligibility(session, input_dict)
    print("done!")
