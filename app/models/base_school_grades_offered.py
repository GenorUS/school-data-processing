from sqlalchemy import Column, String, Float, Date, DateTime, Boolean
from config import PROD_FLG, DB_PROD, DB_DEV
from .base import Base


class BaseSchoolGradesOffered(Base):

    __tablename__ = 'base_school_grades_offered'.lower()
    if PROD_FLG:
        __table_args__ = {'schema': DB_PROD['schema']}
    else:
        __table_args__ = {'schema': DB_DEV['schema']}

    school_id = Column("school_id", String(12), primary_key=True, index=True)
    no_grades = Column("no_grades", String(12))
    g_pk_offered = Column("g_pk_offered", String(12))
    g_kg_offered = Column("g_kg_offered", String(12))
    g_1_offered = Column("g_1_offered", String(12))
    g_2_offered = Column("g_2_offered", String(12))
    g_3_offered = Column("g_3_offered", String(12))
    g_4_offered = Column("g_4_offered", String(12))
    g_5_offered = Column("g_5_offered", String(12))
    g_6_offered = Column("g_6_offered", String(12))
    g_7_offered = Column("g_7_offered", String(12))
    g_8_offered = Column("g_8_offered", String(12))
    g_9_offered = Column("g_9_offered", String(12))
    g_10_offered = Column("g_10_offered", String(12))
    g_11_offered = Column("g_11_offered", String(12))
    g_12_offered = Column("g_12_offered", String(12))
    g_13_offered = Column("g_13_offered", String(12))
    g_ug_offered = Column("g_ug_offered", String(12))
    g_ae_offered = Column("g_ae_offered", String(12))
    g_lowest_offered = Column("g_lowest_offered", String(12))
    g_highest_offered = Column("g_highest_offered", String(12))
    data_year = Column("data_year", String(9))
    inserted_ts = Column("inserted_ts", DateTime)
    updated_ts = Column("updated_ts", DateTime)
