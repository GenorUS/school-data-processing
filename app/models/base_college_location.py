from sqlalchemy import Column, String, Float, DateTime
from .base import Base


class BaseCollegeLocation(Base):

    __tablename__ = 'base_college_location'.lower()

    inst_id = Column('inst_id', Float, primary_key=True, index=True)  # UNITID
    mailing_address1 = Column('mailing_address1', String(100))  # ADDR
    mailing_city = Column('mailing_city', String(30))  # CITY
    mailing_state = Column('mailing_state', String(2))  # STABBR
    mailing_zip = Column('mailing_zip', String(10))  # ZIP
    fips_state_cd = Column('fips_state_cd', Float)  # FIPS
    bea_region = Column('bea_region', Float)  # OBEREG
    urban_locale = Column('urban_locale', Float)  # LOCALE
    cbsa = Column('cbsa', Float)  # CBSA
    cbsa_type = Column('cbsa_type', Float)  # CBSATYPE
    csa = Column('csa', Float)  # CSA
    necta = Column('necta', Float)  # NECTA
    fips_county_cd = Column('fips_county_cd', Float)  # COUNTYCD
    county_nm = Column('county_nm', String(30))  # COUNTYNM
    congress_district_cd = Column('congress_district_cd', Float)  # CNGDSTCD
    longitude = Column('longitude', Float)  # LONGITUD
    latitude = Column('latitude', Float)  # LATITUDE
    inserted_ts = Column("inserted_ts", DateTime)  # INSERTED_TS
    updated_ts = Column("updated_ts", DateTime)  # UPDATED_TS
