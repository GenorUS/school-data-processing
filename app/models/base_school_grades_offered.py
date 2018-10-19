from sqlalchemy import Column, String, Float, Date, DateTime, Boolean
# from config import PROD_FLG, DB_PROD, DB_DEV
from .base import Base


class BaseSchoolGradesOffered(Base):

    __tablename__ = 'base_school_grades_offered'.lower()
    # if PROD_FLG:
    #     __table_args__ = {'schema': DB_PROD['schema']}
    # else:
    #     __table_args__ = {'schema': DB_DEV['schema']}

    school_id = Column("school_id", String(12), primary_key=True, index=True)
    no_grades = Column("no_grades", String(12))
    g_pk_offered = Column("g_pk_offered", Boolean)
    g_kg_offered = Column("g_kg_offered", Boolean)
    g_1_offered = Column("g_1_offered", Boolean)
    g_2_offered = Column("g_2_offered", Boolean)
    g_3_offered = Column("g_3_offered", Boolean)
    g_4_offered = Column("g_4_offered", Boolean)
    g_5_offered = Column("g_5_offered", Boolean)
    g_6_offered = Column("g_6_offered", Boolean)
    g_7_offered = Column("g_7_offered", Boolean)
    g_8_offered = Column("g_8_offered", Boolean)
    g_9_offered = Column("g_9_offered", Boolean)
    g_10_offered = Column("g_10_offered", Boolean)
    g_11_offered = Column("g_11_offered", Boolean)
    g_12_offered = Column("g_12_offered", Boolean)
    g_13_offered = Column("g_13_offered", Boolean)
    g_ug_offered = Column("g_ug_offered", Boolean)
    g_ae_offered = Column("g_ae_offered", Boolean)
    g_lowest_offered = Column("g_lowest_offered", String(2))
    g_highest_offered = Column("g_highest_offered", String(2))
    inserted_ts = Column("inserted_ts", DateTime)
    updated_ts = Column("updated_ts", DateTime)
