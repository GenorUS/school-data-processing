from ..models import *
from datetime import datetime


def load_base_school_def(session):
    
    # delete existing records and reload
    session.query(BaseSchoolDef).delete()

    # get the public school records
    print("processing public school data")
    public_school_records = session.query(JrnlPublicSchoolBase.NCESSCH,
                                          JrnlPublicSchoolBase.SCHID,
                                          JrnlPublicSchoolBase.ST_SCHID,
                                          JrnlPublicSchoolBase.SCH_NAME,
                                          JrnlPublicSchoolBase.LEAID,
                                          JrnlPublicSchoolBase.ST_LEAID,
                                          JrnlPublicSchoolBase.LEA_NAME,
                                          JrnlPublicSchoolBase.UNION,
                                          JrnlPublicSchoolBase.SCH_TYPE_TEXT,
                                          JrnlPublicSchoolBase.LEVEL,
                                          JrnlPublicSchoolStaff.FTE.label('FTE'),
                                          JrnlPublicSchoolBase.CHARTER_TEXT,
                                          JrnlPublicSchoolBase.CHARTAUTHN1,
                                          JrnlPublicSchoolBase.CHARTAUTH1,
                                          JrnlPublicSchoolBase.CHARTAUTHN2,
                                          JrnlPublicSchoolBase.CHARTAUTH2,
                                          JrnlPublicSchoolBase.PHONE,
                                          JrnlPublicSchoolBase.WEBSITE,
                                          JrnlPublicSchoolBase.UPDATED_STATUS_TEXT,
                                          JrnlPublicSchoolBase.RECON_STATUS,
                                          JrnlPublicSchoolBase.EFFECTIVE_DATE,
                                          JrnlPublicSchoolBase.SCHOOL_YEAR,
                                          ).join(JrnlPublicSchoolStaff,
                                                 JrnlPublicSchoolBase.NCESSCH == JrnlPublicSchoolStaff.NCESSCH).all()

    for r in public_school_records:
        record = BaseSchoolDef(school_id=r.NCESSCH,
                                school_nces_id=r.SCHID,
                                school_state_id=r.ST_SCHID,
                                is_private=False,
                                school_name=r.SCH_NAME,
                                nces_agency_id=r.LEAID,
                                state_agency_id=r.ST_LEAID,
                                agency_name=r.LEA_NAME,
                                union_id=r.UNION,
                                school_type=r.SCH_TYPE_TEXT,
                                school_level=r.LEVEL,
                                school_full_time_teachers=float(r.FTE),
                                charter=r.CHARTER_TEXT,
                                charter_auth1_id=r.CHARTAUTHN1,
                                charter_auth1_nm=r.CHARTAUTH1,
                                charter_auth2_id=r.CHARTAUTHN2,
                                charter_auth2_nm=r.CHARTAUTH2,
                                telephone_num=r.PHONE,
                                website_url=r.WEBSITE,
                                status=r.UPDATED_STATUS_TEXT,
                                reconstituted=r.RECON_STATUS,
                                status_dt=r.EFFECTIVE_DATE,
                                data_year=r.SCHOOL_YEAR,
                                inserted_ts=datetime.now(),
                                updated_ts=datetime.now()
                                )
        session.add(record)
    session.commit()
    print("public school processing complete")

    print("processing private school data")
    private_school_records = session.query(JrnlPrivateSchool.PPIN,
                                           JrnlPrivateSchool.PINST,
                                           JrnlPrivateSchool.LEVEL,
                                           JrnlPrivateSchool.NUMTEACH,
                                           ).all()

    for r in private_school_records:
        record = BaseSchoolDef(school_id=r.PPIN,
                                is_private=True,
                                school_name=r.PINST,
                                school_level=r.LEVEL,
                                school_full_time_teachers=float(r.NUMTEACH),
                                status='Open',
                                inserted_ts=datetime.now(),
                                updated_ts=datetime.now()
                                )
        session.add(record)

    session.commit()

    print("private school processing complete")

