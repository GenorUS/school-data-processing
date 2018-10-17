from sqlalchemy import Column, String, Float, Date, DateTime, Boolean
from config import PROD_FLG, DB_PROD, DB_DEV
from .base import Base


class BaseSchoolDef(Base):

    __tablename__ = 'base_school_def'.lower()
    if PROD_FLG:
        __table_args__ = {'schema': DB_PROD['schema']}
    else:
        __table_args__ = {'schema': DB_DEV['schema']}

    school_id = Column("school_id", String(12), primary_key=True, index=True)
    school_nces_id = Column("nces_id", String(5))
    school_state_id = Column("state_id", String(35))
    is_private = Column("is_private", Boolean, default=True)  # set at load time
    school_name = Column("school_nm", String(60))
    nces_agency_id = Column("nces_agency_id", String(7))
    state_agency_id = Column("agency_state_id", String(35))
    agency_name = Column("agency_nm", String(60))
    union_id = Column("union_id", String(3))
    school_type = Column("school_type", String(28))
    school_level = Column("school_level", String(16), index=True)
    school_full_time_teachers = Column('full_time_teachers', Float)
    charter = Column("charter", String(14))
    charter_auth1_id = Column("charter_auth1_id", String(14))
    charter_auth1_nm = Column("charter_auth1_nm", String(60))
    charter_auth2_id = Column("charter_auth2_id", String(14))
    charter_auth2_nm = Column("charter_auth2_nm", String(60))
    telephone_num = Column("telephone_num", String(13))
    website_url = Column("website_url", String(80))
    status = Column("status", String(30))
    reconstituted = ("reconstituted", String(3))
    status_dt = Column("status_dt", Date)
    data_year = Column("data_year", String(9))
    inserted_ts = Column("inserted_ts", DateTime)
    updated_ts = Column("updated_ts", DateTime)
