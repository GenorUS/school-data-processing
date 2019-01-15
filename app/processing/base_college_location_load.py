from ..models import *
from datetime import datetime


def load_base_college_location(session):
    # delete existing records and reload
    session.query(BaseCollegeLocation).delete()

    # get the public school records
    print("processing college location data")

    jrnl_records = session.query(
        JrnlCollegeBase.UNITID,
        JrnlCollegeBase.ADDR,
        JrnlCollegeBase.CITY,
        JrnlCollegeBase.STABBR,
        JrnlCollegeBase.ZIP,
        JrnlCollegeBase.FIPS,
        JrnlCollegeBase.OBEREG,
        JrnlCollegeBase.LOCALE,
        JrnlCollegeBase.CBSA,
        JrnlCollegeBase.CBSATYPE,
        JrnlCollegeBase.CSA,
        JrnlCollegeBase.NECTA,
        JrnlCollegeBase.COUNTYCD,
        JrnlCollegeBase.COUNTYNM,
        JrnlCollegeBase.CNGDSTCD,
        JrnlCollegeBase.LONGITUD,
        JrnlCollegeBase.LATITUDE).all()

    for r in jrnl_records:
        record = BaseCollegeLocation(
            inst_id=r.UNITID,
            mailing_address1=r.ADDR,
            mailing_city=r.CITY,
            mailing_state=r.STABBR,
            mailing_zip=r.ZIP,
            fips_state_cd=r.FIPS,
            bea_region=r.OBEREG,
            urban_locale=r.LOCALE,
            cbsa=r.CBSA,
            cbsa_type=r.CBSATYPE,
            csa=r.CSA,
            necta=r.NECTA,
            fips_county_cd=r.COUNTYCD,
            county_nm=r.COUNTYNM,
            congress_district_cd=r.CNGDSTCD,
            longitude=r.LONGITUD,
            latitude=r.LATITUDE,
            inserted_ts=datetime.now(),
            updated_ts=datetime.now()
        )

        session.add(record)
    session.commit()
    print("college location processing complete")
