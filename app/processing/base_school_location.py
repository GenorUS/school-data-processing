from ..models import *
from datetime import datetime
from .geocoding import Geocoder
from config import MAPQUEST_API_KEY

geo = Geocoder(MAPQUEST_API_KEY)

def load_base_school_location(session):

    # delete existing records and reload
    session.query(BaseSchoolLocation).delete()

    # get the public school records
    print("processing public school data")
    public_school_records = session.query(JrnlPublicSchoolBase.NCESSCH,
                                          JrnlPublicSchoolBase.ST,
                                          JrnlPublicSchoolBase.FIPST,
                                          JrnlPublicSchoolBase.STATENAME,
                                          JrnlPublicSchoolBase.MSTREET1,
                                          JrnlPublicSchoolBase.MSTREET2,
                                          JrnlPublicSchoolBase.MSTREET3,
                                          JrnlPublicSchoolBase.MCITY,
                                          JrnlPublicSchoolBase.MSTATE,
                                          JrnlPublicSchoolBase.MZIP,
                                          JrnlPublicSchoolBase.MZIP4,
                                          JrnlPublicSchoolBase.LSTREET1,
                                          JrnlPublicSchoolBase.LSTREET2,
                                          JrnlPublicSchoolBase.LSTREET3,
                                          JrnlPublicSchoolBase.LCITY,
                                          JrnlPublicSchoolBase.LSTATE,
                                          JrnlPublicSchoolBase.LZIP,
                                          JrnlPublicSchoolBase.LZIP4,
                                          JrnlPublicSchoolBase.OUT_OF_STATE_FLAG
                                          ).all()

    for r in public_school_records:
        # check for location data, else use mailing data
        loc_str1 = r.LSTREET1 if r.LSTREET1 else r.MSTREET1
        loc_str2 = r.LSTREET2 if r.LSTREET2 else r.MSTREET2
        loc_str3 = r.LSTREET3 if r.LSTREET3 else r.MSTREET3
        loc_city = r.LCITY if r.LCITY else r.MCITY
        loc_state = r.LSTATE if r.LSTATE else r.MSTATE
        loc_zip = r.LZIP if r.LZIP else r.MZIP
        
        # get the lat / lng for the address
        coords = geo.get_coords(loc_str1, loc_city, loc_state, loc_zip)

        record = BaseSchoolLocation(school_id=r.NCESSCH,
                                    state=r.ST,
                                    ansi_state=r.FIPST,
                                    state_nm=r.STATENAME,
                                    mailing_street1=r.MSTREET1,
                                    mailing_street2=r.MSTREET2,
                                    mailing_street3=r.MSTREET3,
                                    mailing_city=r.MCITY,
                                    mailing_state=r.MSTATE,
                                    mailing_zip=r.MZIP,
                                    mailing_zip4=r.MZIP4,
                                    location_street1=loc_str1,
                                    location_street2=loc_str2,
                                    location_street3=loc_str3,
                                    location_city=loc_city,
                                    location_state=loc_state,
                                    location_zip=loc_zip,
                                    location_zip4=r.LZIP4,
                                    latitude=coords['lat'],
                                    longitude=coords['lng'],
                                    out_of_state_flg=r.OUT_OF_STATE_FLAG,
                                    inserted_ts=datetime.now(),
                                    updated_ts=datetime.now()
                                    )
        session.add(record)

    session.commit()
    print("public school processing complete")
    print("processing private school data")

    private_school_records = session.query(JrnlPrivateSchool.PPIN,
                                           JrnlPrivateSchool.PSTANSI,
                                           JrnlPrivateSchool.PADDRS,
                                           JrnlPrivateSchool.PCITY,
                                           JrnlPrivateSchool.PSTABB,
                                           JrnlPrivateSchool.PZIP,
                                           JrnlPrivateSchool.PZIP4,
                                           JrnlPrivateSchool.PL_ADD,
                                           JrnlPrivateSchool.PL_CIT,
                                           JrnlPrivateSchool.PL_STABB,
                                           JrnlPrivateSchool.PL_ZIP,
                                           JrnlPrivateSchool.PL_ZIP4,
                                           JrnlPrivateSchool.LATITUDE16,
                                           JrnlPrivateSchool.LONGITUDE16
                                           ).all()

    for r in private_school_records:
        record = BaseSchoolLocation(school_id=r.PPIN,
                                    state=r.PSTANSI,
                                    ansi_state=r.PSTANSI,
                                    mailing_street1=r.PADDRS,
                                    mailing_city=r.PCITY,
                                    mailing_state=r.PSTABB,
                                    mailing_zip=r.PZIP,
                                    mailing_zip4=r.PZIP4,
                                    location_street1=r.PL_ADD if r.PL_ADD else r.PADDRS,
                                    location_city=r.PL_CIT if r.PL_CIT else r.PCITY,
                                    location_state=r.PL_STABB if r.PL_STABB else r.PSTABB,
                                    location_zip=r.PL_ZIP if r.PL_ZIP else r.PZIP,
                                    location_zip4=r.PL_ZIP4 if r.PL_ZIP4 else r.PZIP4,
                                    latitude=r.LATITUDE16,
                                    longitude=r.LONGITUDE16,
                                    out_of_state_flg="No",
                                    inserted_ts=datetime.now(),
                                    updated_ts=datetime.now()
                                    )
        session.add(record)

    session.commit()

    print("private school processing complete")
