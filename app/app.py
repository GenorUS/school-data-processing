from .models import *
from .processing import *


def create_session(db_dict):
    mysql_session(db_dict)


# private high school journal load

def load_private_school(session, input_dict):
    input_file = input_dict['private']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlPrivateSchool(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


# public high school journal load

def load_public_school_base(session, input_dict):
    input_file = input_dict['public_base']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlPublicSchoolBase(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_public_school_characteristics(session, input_dict):
    input_file = input_dict['public_char']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlPublicSchoolCharacteristics(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_public_school_eligibility(session, input_dict):
    input_file = input_dict['public_elig']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlPublicSchoolEligibility(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_public_school_membership(session, input_dict):
    input_file = input_dict['public_mem']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlPublicSchoolMembership(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_public_school_staff(session, input_dict):
    input_file = input_dict['public_staff']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlPublicSchoolStaff(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


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


# college data journal load

def load_college_base(session, input_dict):
    input_file = input_dict['college_base']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlCollegeBase(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_college_academic_charges(session, input_dict):
    input_file = input_dict['college_academic_charges']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlCollegeAcademicCharges(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_college_activity(session, input_dict):
    input_file = input_dict['college_activity']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlCollegeActivity(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_college_enrollment(session, input_dict):
    input_file = input_dict['college_enrollment']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlCollegeEnrollment(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_college_offering(session, input_dict):
    input_file = input_dict['college_offering']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlCollegeOffering(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_college_program_charges(session, input_dict):
    input_file = input_dict['college_program_charges']
    data = csv_to_dicts(input_file)
    counter = 0
    for i in data:
        record = JrnlCollegeProgramCharges(**i)
        session.add(record)
        counter += 1
        if counter % 1000 == 0:
            session.commit()
    session.commit()
    print("{} records inserted/updated".format(counter))


def load_college_all(session, input_dict):
    print("loading jrnl_college_base")
    load_college_base(session, input_dict)
    print("loading jrnl_college_academic_charges")
    load_college_academic_charges(session, input_dict)
    print("loading jrnl_college_activity")
    load_college_activity(session, input_dict)
    print("loading jrnl_college_enrollment")
    load_college_enrollment(session, input_dict)
    print("loading jrnl_college_offering")
    load_college_offering(session, input_dict)
    print("loading jrnl_college_program_charges")
    load_college_program_charges(session, input_dict)

    print("college load successful!")

def process_base_school_def(session):

    load_base_school_def(session)
    load_base_school_location(session)
    load_base_grades_offered(session)
