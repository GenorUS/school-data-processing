from sqlalchemy import Column, String, Float, DateTime
from .base import Base


class BaseCollegeBase(Base):

    __tablename__ = 'base_college_base'.lower()

    inst_id = Column('inst_id', Float, primary_key=True, index=True)  # UNITID
    inst_nm = Column('inst_nm', String(120))  # INSTNM
    inst_alias = Column('inst_alias', String(2000))  # IALIAS
    chief_admin_nm = Column('chief_admin_nm', String(50))  # CHFNM
    chief_admin_title = Column('chief_admin_title', String(50))  # CHFTITLE
    general_telephone_num = Column('general_telephone_num', String(15))  # GENTELE
    ein = Column('ein', String(9))  # EIN
    dun_bradstreet_num = Column('dun_bradstreet_num', String(2000))  # DUNS
    ope_id = Column('ope_id', String(8))  # OPEID
    ope_title4_flg = Column('ope_title4_flg', Float)  # OPEFLAG
    url_general = Column('url_general', String(150))  # WEBADDR
    url_admissions = Column('url_admissions', String(200))  # ADMINURL
    url_financial_aid = Column('url_financial_aid', String(200))  # FAIDURL
    url_application = Column('url_application', String(200))  # APPLURL
    url_net_price_calculator = Column('url_net_price_calculator', String(200))  # NPRICURL
    url_veterans = Column('url_veterans', String(200))  # VETURL
    url_athlete_grad_rate = Column('url_athlete_grad_rate', String(150))  # ATHURL
    url_disability = Column('url_disability', String(200))  # DISAURL
    inst_sector = Column('inst_sector', Float)  # SECTOR
    inst_level = Column('inst_level', Float)  # ICLEVEL
    inst_control = Column('inst_control', Float)  # CONTROL
    level_highest_offering = Column('level_highest_offering', Float)  # HLOFFER
    undergrad_offering = Column('undergrad_offering', Float)  # UGOFFER
    grad_offering = Column('grad_offering', Float)  # GROFFER
    degree_highest_offered = Column('degree_highest_offered', Float)  # HDEGOFR1
    degree_granting_status = Column('degree_granting_status', Float)  # DEGGRANT
    hbcu_flg = Column('hbcu_flg', Float)  # HBCU
    hospital_flg = Column('hospital_flg', Float)  # HOSPITAL
    medical_degree_flg = Column('medical_degree_flg', Float)  # MEDICAL
    tribal_inst_flg = Column('tribal_inst_flg', Float)  # TRIBAL
    open_to_general_public = Column('open_to_general_public', Float)  # OPENPUBL
    ipeds_participation = Column('ipeds_participation', String(1))  # ACT
    merged_inst_id = Column('merged_inst_id', Float)  # NEWID
    ipeds_removal_yr = Column('ipeds_removal_yr', Float)  # DEATHYR
    inst_closed_dt = Column('inst_closed_dt', String(10))  # CLOSEDAT
    inst_curr_active_flg = Column('inst_curr_active_flg', Float)  # CYACTIVE
    post_secondary_only = Column('post_secondary_only', Float)  # POSTSEC
    post_secondary_flg = Column('post_secondary_flg', Float)  # PSEFLAG
    agg_type_flg = Column('agg_type_flg', Float)  # PSET4FLG
    reporting_method = Column('reporting_method', Float)  # RPTMTH
    inst_category = Column('inst_category', Float)  # INSTCAT
    carnegie_basic_class_shorthand = Column('carnegie_basic_class_shorthand', Float)  # C15BASIC
    carnegie_undergrad_focus = Column('carnegie_undergrad_focus', Float)  # C15IPUG
    carnegie_grad_focus = Column('carnegie_grad_focus', Float)  # C15IPGRD
    carnegie_undergrad_profile = Column('carnegie_undergrad_profile', Float)  # C15UGPRF
    carnegie_enrollment_profile = Column('carnegie_enrollment_profile', Float)  # C15ENPRF
    carnegie_setting_classification = Column('carnegie_setting_classification', Float)  # C15SZSET
    carnegie_basic_classification = Column('CCBASIC', Float)  # CCBASIC
    carnegie_classification = Column('carnegie_classification', Float)  # CARNEGIE
    land_grant_inst = Column('land_grant_inst', Float)  # LANDGRNT
    inst_size_category = Column('inst_size_category', Float)  # INSTSIZE
    multi_inst_flg = Column('multi_inst_flg', Float)  # F1SYSTYP
    multi_inst_nm = Column('multi_inst_nm', String(80))  # F1SYSNAM
    multi_inst_id = Column('multi_inst_id', String(6))  # F1SYSCOD
    inserted_ts = Column("inserted_ts", DateTime)  # INSERTED_TS
    updated_ts = Column("updated_ts", DateTime)  # UPDATED_TS
