from sqlalchemy import Column, String, Float, Date, DateTime, Boolean
# from config import PROD_FLG, DB_PROD, DB_DEV
from .base import Base


class BaseSchoolLocation(Base):

    __tablename__ = 'base_school_location'.lower()
    # if PROD_FLG:
    #     __table_args__ = {'schema': DB_PROD['schema']}
    # else:
    #     __table_args__ = {'schema': DB_DEV['schema']}

    school_id = Column("school_id", String(12), primary_key=True, index=True)
    state = Column("state", String(2))
    ansi_state = Column("ansi_state", String(2))
    state_nm = Column("state_nm", String(44))
    mailing_street1 = Column("mailing_street1", String(60))
    mailing_street2 = Column("mailing_street2", String(60))
    mailing_street3 = Column("mailing_street3", String(60))
    mailing_city = Column("mailing_city", String(30))
    mailing_state = Column("mailing_state", String(2))
    mailing_zip = Column("mailing_zip", String(5))
    mailing_zip4 = Column("mailing_zip4", String(4))
    location_street1 = Column("location_street1", String(60))
    location_street2 = Column("location_street2", String(60))
    location_street3 = Column("location_street3", String(60))
    location_city = Column("location_city", String(30))
    location_state = Column("location_state", String(2))
    location_zip = Column("location_zip", String(5))
    location_zip4 = Column("location_zip4", String(4))
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
    out_of_state_flg = Column("out_of_state_flg", String(3))
    inserted_ts = Column("inserted_ts", DateTime)
    updated_ts = Column("updated_ts", DateTime)