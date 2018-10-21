from sqlalchemy import Column, Float, DateTime, String
from .base import Base

# https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx


class JrnlCollegeOffering(Base):

    __tablename__ = 'jrnl_college_offerings'.lower()

    UNITID = Column('UNITID', Float, primary_key=True, index=True)
    PEO1ISTR = Column('PEO1ISTR', Float)
    PEO2ISTR = Column('PEO2ISTR', Float)
    PEO3ISTR = Column('PEO3ISTR', Float)
    PEO4ISTR = Column('PEO4ISTR', Float)
    PEO5ISTR = Column('PEO5ISTR', Float)
    PEO6ISTR = Column('PEO6ISTR', Float)
    CNTLAFFI = Column('CNTLAFFI', Float)
    PUBPRIME = Column('PUBPRIME', Float)
    PUBSECON = Column('PUBSECON', Float)
    RELAFFIL = Column('RELAFFIL', Float)
    LEVEL1 = Column('LEVEL1', Float)
    LEVEL2 = Column('LEVEL2', Float)
    LEVEL3 = Column('LEVEL3', Float)
    LEVEL4 = Column('LEVEL4', Float)
    LEVEL5 = Column('LEVEL5', Float)
    LEVEL6 = Column('LEVEL6', Float)
    LEVEL7 = Column('LEVEL7', Float)
    LEVEL8 = Column('LEVEL8', Float)
    LEVEL12 = Column('LEVEL12', Float)
    LEVEL17 = Column('LEVEL17', Float)
    LEVEL18 = Column('LEVEL18', Float)
    LEVEL19 = Column('LEVEL19', Float)
    CALSYS = Column('CALSYS', Float)
    FT_UG = Column('FT_UG', Float)
    FT_FTUG = Column('FT_FTUG', Float)
    FTGDNIDP = Column('FTGDNIDP', Float)
    PT_UG = Column('PT_UG', Float)
    PT_FTUG = Column('PT_FTUG', Float)
    PTGDNIDP = Column('PTGDNIDP', Float)
    DOCPP = Column('DOCPP', Float)
    DOCPPSP = Column('DOCPPSP', Float)
    OPENADMP = Column('OPENADMP', Float)
    VET1 = Column('VET1', Float)
    VET2 = Column('VET2', Float)
    VET3 = Column('VET3', Float)
    VET4 = Column('VET4', Float)
    VET5 = Column('VET5', Float)
    VET9 = Column('VET9', Float)
    CREDITS1 = Column('CREDITS1', Float)
    CREDITS2 = Column('CREDITS2', Float)
    CREDITS3 = Column('CREDITS3', Float)
    CREDITS4 = Column('CREDITS4', Float)
    SLO5 = Column('SLO5', Float)
    SLO51 = Column('SLO51', Float)
    SLO52 = Column('SLO52', Float)
    SLO53 = Column('SLO53', Float)
    SLO6 = Column('SLO6', Float)
    SLO7 = Column('SLO7', Float)
    SLO8 = Column('SLO8', Float)
    SLO81 = Column('SLO81', Float)
    SLO82 = Column('SLO82', Float)
    SLO83 = Column('SLO83', Float)
    SLO9 = Column('SLO9', Float)
    YRSCOLL = Column('YRSCOLL', Float)
    STUSRV1 = Column('STUSRV1', Float)
    STUSRV2 = Column('STUSRV2', Float)
    STUSRV3 = Column('STUSRV3', Float)
    STUSRV4 = Column('STUSRV4', Float)
    STUSRV8 = Column('STUSRV8', Float)
    STUSRV9 = Column('STUSRV9', Float)
    LIBRES1 = Column('LIBRES1', Float)
    LIBRES2 = Column('LIBRES2', Float)
    LIBRES3 = Column('LIBRES3', Float)
    LIBRES4 = Column('LIBRES4', Float)
    LIBRES5 = Column('LIBRES5', Float)
    LIBRES6 = Column('LIBRES6', Float)
    LIBRES9 = Column('LIBRES9', Float)
    TUITPL = Column('TUITPL', Float)
    TUITPL1 = Column('TUITPL1', Float)
    TUITPL2 = Column('TUITPL2', Float)
    TUITPL3 = Column('TUITPL3', Float)
    TUITPL4 = Column('TUITPL4', Float)
    DSTNUGC = Column('DSTNUGC', Float)
    DSTNUGP = Column('DSTNUGP', Float)
    DSTNUGN = Column('DSTNUGN', Float)
    DSTNGC = Column('DSTNGC', Float)
    DSTNGP = Column('DSTNGP', Float)
    DSTNGN = Column('DSTNGN', Float)
    DISTCRS = Column('DISTCRS', Float)
    DISTPGS = Column('DISTPGS', Float)
    DSTNCED1 = Column('DSTNCED1', Float)
    DSTNCED2 = Column('DSTNCED2', Float)
    DSTNCED3 = Column('DSTNCED3', Float)
    DISTNCED = Column('DISTNCED', Float)
    DISAB = Column('DISAB', Float)
    DISABPCT = Column('DISABPCT', Float)
    ALLONCAM = Column('ALLONCAM', Float)
    TUITVARY = Column('TUITVARY', Float)
    ROOM = Column('ROOM', Float)
    ROOMCAP = Column('ROOMCAP', Float)
    BOARD = Column('BOARD', Float)
    MEALSWK = Column('MEALSWK', Float)
    ROOMAMT = Column('ROOMAMT', Float)
    BOARDAMT = Column('BOARDAMT', Float)
    RMBRDAMT = Column('RMBRDAMT', Float)
    APPLFEEU = Column('APPLFEEU', Float)
    APPLFEEG = Column('APPLFEEG', Float)
    ATHASSOC = Column('ATHASSOC', Float)
    ASSOC1 = Column('ASSOC1', Float)
    ASSOC2 = Column('ASSOC2', Float)
    ASSOC3 = Column('ASSOC3', Float)
    ASSOC4 = Column('ASSOC4', Float)
    ASSOC5 = Column('ASSOC5', Float)
    ASSOC6 = Column('ASSOC6', Float)
    SPORT1 = Column('SPORT1', Float)
    CONFNO1 = Column('CONFNO1', Float)
    SPORT2 = Column('SPORT2', Float)
    CONFNO2 = Column('CONFNO2', Float)
    SPORT3 = Column('SPORT3', Float)
    CONFNO3 = Column('CONFNO3', Float)
    SPORT4 = Column('SPORT4', Float)
    CONFNO4 = Column('CONFNO4', Float)
    XDISABPC = Column('XDISABPC', String(1))
    XROOMCAP = Column('XROOMCAP', String(1))
    XMEALSWK = Column('XMEALSWK', String(1))
    XROOMAMT = Column('XROOMAMT', String(1))
    XBORDAMT = Column('XBORDAMT', String(1))
    XRMBDAMT = Column('XRMBDAMT', String(1))
    XAPPFEEU = Column('XAPPFEEU', String(1))
    XAPPFEEG = Column('XAPPFEEG', String(1))
    INSERTED_TS = Column("INSERTED_TS", DateTime)
    UPDATED_TS = Column("UPDATED_TS", DateTime)