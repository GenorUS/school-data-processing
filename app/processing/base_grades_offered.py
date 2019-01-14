from ..models import *
from datetime import datetime


def load_base_grades_offered(session):

    # get the public school records
    print("processing public school data")
    public_school_records = session.query(JrnlPublicSchoolBase.NCESSCH,
                                          JrnlPublicSchoolBase.NOGRADES,
                                          JrnlPublicSchoolBase.G_PK_OFFERED,
                                          JrnlPublicSchoolBase.G_KG_OFFERED,
                                          JrnlPublicSchoolBase.G_1_OFFERED,
                                          JrnlPublicSchoolBase.G_2_OFFERED,
                                          JrnlPublicSchoolBase.G_3_OFFERED,
                                          JrnlPublicSchoolBase.G_4_OFFERED,
                                          JrnlPublicSchoolBase.G_5_OFFERED,
                                          JrnlPublicSchoolBase.G_6_OFFERED,
                                          JrnlPublicSchoolBase.G_7_OFFERED,
                                          JrnlPublicSchoolBase.G_8_OFFERED,
                                          JrnlPublicSchoolBase.G_9_OFFERED,
                                          JrnlPublicSchoolBase.G_10_OFFERED,
                                          JrnlPublicSchoolBase.G_11_OFFERED,
                                          JrnlPublicSchoolBase.G_12_OFFERED,
                                          JrnlPublicSchoolBase.G_13_OFFERED,
                                          JrnlPublicSchoolBase.G_UG_OFFERED,
                                          JrnlPublicSchoolBase.G_AE_OFFERED,
                                          JrnlPublicSchoolBase.GSLO,
                                          JrnlPublicSchoolBase.GSHI
                                          ).all()

    for r in public_school_records:

        res = session.query(BaseSchoolGradesOffered).filter(BaseSchoolGradesOffered.school_id == r.NCESSCH).first()

        if res:
            res.no_grades = grade_offering_to_bool(r.NOGRADES)
            res.g_pk_offered = grade_offering_to_bool(r.G_PK_OFFERED)
            res.g_kg_offered = grade_offering_to_bool(r.G_KG_OFFERED)
            res.g_1_offered = grade_offering_to_bool(r.G_1_OFFERED)
            res.g_2_offered = grade_offering_to_bool(r.G_2_OFFERED)
            res.g_3_offered = grade_offering_to_bool(r.G_3_OFFERED)
            res.g_4_offered = grade_offering_to_bool(r.G_4_OFFERED)
            res.g_5_offered = grade_offering_to_bool(r.G_5_OFFERED)
            res.g_6_offered = grade_offering_to_bool(r.G_6_OFFERED)
            res.g_7_offered = grade_offering_to_bool(r.G_7_OFFERED)
            res.g_8_offered = grade_offering_to_bool(r.G_8_OFFERED)
            res.g_9_offered = grade_offering_to_bool(r.G_9_OFFERED)
            res.g_10_offered = grade_offering_to_bool(r.G_10_OFFERED)
            res.g_11_offered = grade_offering_to_bool(r.G_11_OFFERED)
            res.g_12_offered = grade_offering_to_bool(r.G_12_OFFERED)
            res.g_13_offered = grade_offering_to_bool(r.G_13_OFFERED)
            res.g_ug_offered = grade_offering_to_bool(r.G_UG_OFFERED)
            res.g_ae_offered = grade_offering_to_bool(r.G_AE_OFFERED)
            res.g_lowest_offered = r.GSLO
            res.g_highest_offered = r.GSHI
            res.updated_ts = datetime.now()

            session.add(res)

        else:

            record = BaseSchoolGradesOffered(school_id=r.NCESSCH,
                                             no_grades=grade_offering_to_bool(r.NOGRADES),
                                             g_pk_offered=grade_offering_to_bool(r.G_PK_OFFERED),
                                             g_kg_offered=grade_offering_to_bool(r.G_KG_OFFERED),
                                             g_1_offered=grade_offering_to_bool(r.G_1_OFFERED),
                                             g_2_offered=grade_offering_to_bool(r.G_2_OFFERED),
                                             g_3_offered=grade_offering_to_bool(r.G_3_OFFERED),
                                             g_4_offered=grade_offering_to_bool(r.G_4_OFFERED),
                                             g_5_offered=grade_offering_to_bool(r.G_5_OFFERED),
                                             g_6_offered=grade_offering_to_bool(r.G_6_OFFERED),
                                             g_7_offered=grade_offering_to_bool(r.G_7_OFFERED),
                                             g_8_offered=grade_offering_to_bool(r.G_8_OFFERED),
                                             g_9_offered=grade_offering_to_bool(r.G_9_OFFERED),
                                             g_10_offered=grade_offering_to_bool(r.G_10_OFFERED),
                                             g_11_offered=grade_offering_to_bool(r.G_11_OFFERED),
                                             g_12_offered=grade_offering_to_bool(r.G_12_OFFERED),
                                             g_13_offered=grade_offering_to_bool(r.G_13_OFFERED),
                                             g_ug_offered=grade_offering_to_bool(r.G_UG_OFFERED),
                                             g_ae_offered=grade_offering_to_bool(r.G_AE_OFFERED),
                                             g_lowest_offered=r.GSLO,
                                             g_highest_offered=r.GSHI,
                                             inserted_ts=datetime.now(),
                                             updated_ts=datetime.now()
                                             )
            session.add(record)

    session.commit()
    print("public school processing complete")
    print("processing private school data")

    private_school_records = session.query(JrnlPrivateSchool.PPIN,
                                           JrnlPrivateSchool.P135,
                                           JrnlPrivateSchool.P145,
                                           JrnlPrivateSchool.P155,
                                           JrnlPrivateSchool.P185,
                                           JrnlPrivateSchool.P195,
                                           JrnlPrivateSchool.P205,
                                           JrnlPrivateSchool.P215,
                                           JrnlPrivateSchool.P225,
                                           JrnlPrivateSchool.P235,
                                           JrnlPrivateSchool.P245,
                                           JrnlPrivateSchool.P255,
                                           JrnlPrivateSchool.P265,
                                           JrnlPrivateSchool.P275,
                                           JrnlPrivateSchool.P285,
                                           JrnlPrivateSchool.P295
                                           ).all()

    for r in private_school_records:
        res = session.query(BaseSchoolGradesOffered).filter(BaseSchoolGradesOffered.school_id == r.PPIN).first()

        if res:
            res.no_grades = grade_offering_to_bool(r.P135)
            res.g_pk_offered = grade_offering_to_bool(r.P145)
            res.g_kg_offered = grade_offering_to_bool(r.P155)
            res.g_1_offered = grade_offering_to_bool(r.P185)
            res.g_2_offered = grade_offering_to_bool(r.P195)
            res.g_3_offered = grade_offering_to_bool(r.P205)
            res.g_4_offered = grade_offering_to_bool(r.P215)
            res.g_5_offered = grade_offering_to_bool(r.P225)
            res.g_6_offered = grade_offering_to_bool(r.P235)
            res.g_7_offered = grade_offering_to_bool(r.P245)
            res.g_8_offered = grade_offering_to_bool(r.P255)
            res.g_9_offered = grade_offering_to_bool(r.P265)
            res.g_10_offered = grade_offering_to_bool(r.P275)
            res.g_11_offered = grade_offering_to_bool(r.P285)
            res.g_12_offered = grade_offering_to_bool(r.P295)
            res.g_lowest_offered = lowest_grade_private(r)
            res.g_highest_offered = highest_grade_private(r)
            res.updated_ts = datetime.now()

            session.add(res)

        else:
            record = BaseSchoolGradesOffered(school_id=r.PPIN,
                                             no_grades=grade_offering_to_bool(r.P135),
                                             g_pk_offered=grade_offering_to_bool(r.P145),
                                             g_kg_offered=grade_offering_to_bool(r.P155),
                                             g_1_offered=grade_offering_to_bool(r.P185),
                                             g_2_offered=grade_offering_to_bool(r.P195),
                                             g_3_offered=grade_offering_to_bool(r.P205),
                                             g_4_offered=grade_offering_to_bool(r.P215),
                                             g_5_offered=grade_offering_to_bool(r.P225),
                                             g_6_offered=grade_offering_to_bool(r.P235),
                                             g_7_offered=grade_offering_to_bool(r.P245),
                                             g_8_offered=grade_offering_to_bool(r.P255),
                                             g_9_offered=grade_offering_to_bool(r.P265),
                                             g_10_offered=grade_offering_to_bool(r.P275),
                                             g_11_offered=grade_offering_to_bool(r.P285),
                                             g_12_offered=grade_offering_to_bool(r.P295),
                                             g_lowest_offered=lowest_grade_private(r),
                                             g_highest_offered=highest_grade_private(r),
                                             inserted_ts=datetime.now(),
                                             updated_ts=datetime.now()
                                             )
            session.add(record)

    session.commit()

    print("private school processing complete")


def grade_offering_to_bool(val):
    if val in [2, "2", "No"]:
        return False
    elif val in [1, "1", "Yes"]:
        return True
    else:
        return None


def highest_grade_private(res_dict):
    if grade_offering_to_bool(res_dict.P295):
        return '12'
    elif grade_offering_to_bool(res_dict.P285):
        return '11'
    elif grade_offering_to_bool(res_dict.P275):
        return '10'
    elif grade_offering_to_bool(res_dict.P265):
        return '09'
    elif grade_offering_to_bool(res_dict.P255):
        return '08'
    elif grade_offering_to_bool(res_dict.P245):
        return '07'
    elif grade_offering_to_bool(res_dict.P235):
        return '06'
    elif grade_offering_to_bool(res_dict.P225):
        return '05'
    elif grade_offering_to_bool(res_dict.P215):
        return '04'
    elif grade_offering_to_bool(res_dict.P205):
        return '03'
    elif grade_offering_to_bool(res_dict.P195):
        return '02'
    elif grade_offering_to_bool(res_dict.P185):
        return '01'
    elif grade_offering_to_bool(res_dict.P155):
        return 'KG'
    elif grade_offering_to_bool(res_dict.P145):
        return 'PK'
    else:
        return None


def lowest_grade_private(res_dict):
    if grade_offering_to_bool(res_dict.P145):
        return 'PK'
    elif grade_offering_to_bool(res_dict.P155):
        return 'KG'
    elif grade_offering_to_bool(res_dict.P185):
        return '01'
    elif grade_offering_to_bool(res_dict.P195):
        return '02'
    elif grade_offering_to_bool(res_dict.P205):
        return '03'
    elif grade_offering_to_bool(res_dict.P215):
        return '04'
    elif grade_offering_to_bool(res_dict.P225):
        return '05'
    elif grade_offering_to_bool(res_dict.P235):
        return '06'
    elif grade_offering_to_bool(res_dict.P245):
        return '07'
    elif grade_offering_to_bool(res_dict.P255):
        return '08'
    elif grade_offering_to_bool(res_dict.P265):
        return '09'
    elif grade_offering_to_bool(res_dict.P275):
        return '10'
    elif grade_offering_to_bool(res_dict.P285):
        return '11'
    elif grade_offering_to_bool(res_dict.P295):
        return '12'
    else:
        return None
