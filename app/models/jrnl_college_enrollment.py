from sqlalchemy import Column, String, Float, DateTime
from .base import Base

# https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx


class JrnlCollegeEnrollment(Base):

    __tablename__ = 'jrnl_college_enrollment'.lower()

    UNITID = Column('UNITID', Float, primary_key=True, index=True)
    EFFYLEV = Column('EFFYLEV', Float)
    LSTUDY = Column('LSTUDY', Float)
    EFYTOTLT = Column('EFYTOTLT', Float)
    EFYTOTLM = Column('EFYTOTLM', Float)
    EFYTOTLW = Column('EFYTOTLW', Float)
    EFYAIANT = Column('EFYAIANT', Float)
    EFYAIANM = Column('EFYAIANM', Float)
    EFYAIANW = Column('EFYAIANW', Float)
    EFYASIAT = Column('EFYASIAT', Float)
    EFYASIAM = Column('EFYASIAM', Float)
    EFYASIAW = Column('EFYASIAW', Float)
    EFYBKAAT = Column('EFYBKAAT', Float)
    EFYBKAAM = Column('EFYBKAAM', Float)
    EFYBKAAW = Column('EFYBKAAW', Float)
    EFYHISPT = Column('EFYHISPT', Float)
    EFYHISPM = Column('EFYHISPM', Float)
    EFYHISPW = Column('EFYHISPW', Float)
    EFYNHPIT = Column('EFYNHPIT', Float)
    EFYNHPIM = Column('EFYNHPIM', Float)
    EFYNHPIW = Column('EFYNHPIW', Float)
    EFYWHITT = Column('EFYWHITT', Float)
    EFYWHITM = Column('EFYWHITM', Float)
    EFYWHITW = Column('EFYWHITW', Float)
    EFY2MORT = Column('EFY2MORT', Float)
    EFY2MORM = Column('EFY2MORM', Float)
    EFY2MORW = Column('EFY2MORW', Float)
    EFYUNKNT = Column('EFYUNKNT', Float)
    EFYUNKNM = Column('EFYUNKNM', Float)
    EFYUNKNW = Column('EFYUNKNW', Float)
    EFYNRALT = Column('EFYNRALT', Float)
    EFYNRALM = Column('EFYNRALM', Float)
    EFYNRALW = Column('EFYNRALW', Float)
    INSERTED_TS = Column("INSERTED_TS", DateTime)
    UPDATED_TS = Column("UPDATED_TS", DateTime)
