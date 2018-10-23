from ..models import *
from datetime import datetime


def load_base_college_def(session):

    # get the public school records
    print("processing college data")
    jrnl_records = session.query(
        JrnlCollegeBase.UNITID,
        JrnlCollegeBase.INSTNM,
        JrnlCollegeBase.IALIAS,
        JrnlCollegeBase.CHFNM,
        JrnlCollegeBase.CHFTITLE,
        JrnlCollegeBase.GENTELE,
        JrnlCollegeBase.EIN,
        JrnlCollegeBase.DUNS,
        JrnlCollegeBase.OPEID,
        JrnlCollegeBase.OPEFLAG,
        JrnlCollegeBase.WEBADDR,
        JrnlCollegeBase.ADMINURL,
        JrnlCollegeBase.FAIDURL,
        JrnlCollegeBase.APPLURL,
        JrnlCollegeBase.NPRICURL,
        JrnlCollegeBase.VETURL,
        JrnlCollegeBase.ATHURL,
        JrnlCollegeBase.DISAURL,
        JrnlCollegeBase.SECTOR,
        JrnlCollegeBase.ICLEVEL,
        JrnlCollegeBase.CONTROL,
        JrnlCollegeBase.HLOFFER,
        JrnlCollegeBase.UGOFFER,
        JrnlCollegeBase.GROFFER,
        JrnlCollegeBase.HDEGOFR1,
        JrnlCollegeBase.DEGGRANT,
        JrnlCollegeBase.HBCU,
        JrnlCollegeBase.HOSPITAL,
        JrnlCollegeBase.MEDICAL,
        JrnlCollegeBase.TRIBAL,
        JrnlCollegeBase.OPENPUBL,
        JrnlCollegeBase.ACT,
        JrnlCollegeBase.NEWID,
        JrnlCollegeBase.DEATHYR,
        JrnlCollegeBase.CLOSEDAT,
        JrnlCollegeBase.CYACTIVE,
        JrnlCollegeBase.POSTSEC,
        JrnlCollegeBase.PSEFLAG,
        JrnlCollegeBase.PSET4FLG,
        JrnlCollegeBase.RPTMTH,
        JrnlCollegeBase.INSTCAT,
        JrnlCollegeBase.C15BASIC,
        JrnlCollegeBase.C15IPUG,
        JrnlCollegeBase.C15IPGRD,
        JrnlCollegeBase.C15UGPRF,
        JrnlCollegeBase.C15ENPRF,
        JrnlCollegeBase.C15SZSET,
        JrnlCollegeBase.CCBASIC,
        JrnlCollegeBase.CARNEGIE,
        JrnlCollegeBase.LANDGRNT,
        JrnlCollegeBase.INSTSIZE,
        JrnlCollegeBase.F1SYSTYP,
        JrnlCollegeBase.F1SYSNAM,
        JrnlCollegeBase.F1SYSCOD).all()

    for r in jrnl_records:

        res = session.query(BaseCollegeBase).filter(BaseCollegeBase.inst_id == r.UNITID).first()

        if res:

            res.inst_nm = r.INSTNM
            res.inst_alias = r.IALIAS
            res.chief_admin_nm = r.CHFNM
            res.chief_admin_title = r.CHFTITLE
            res.general_telephone_num = r.GENTELE
            res.ein = r.EIN
            res.dun_bradstreet_num = r.DUNS
            res.ope_id = r.OPEID
            res.ope_title4_flg = r.OPEFLAG
            res.url_general = r.WEBADDR
            res.url_admissions = r.ADMINURL
            res.url_financial_aid = r.FAIDURL
            res.url_application = r.APPLURL
            res.url_net_price_calculator = r.NPRICURL
            res.url_veterans = r.VETURL
            res.url_athlete_grad_rate = r.ATHURL
            res.url_disability = r.DISAURL
            res.inst_sector = r.SECTOR
            res.inst_level = r.ICLEVEL
            res.inst_control = r.CONTROL
            res.level_highest_offering = r.HLOFFER
            res.undergrad_offering = r.UGOFFER
            res.grad_offering = r.GROFFER
            res.degree_highest_offered = r.HDEGOFR1
            res.degree_granting_status = r.DEGGRANT
            res.hbcu_flg = r.HBCU
            res.hospital_flg = r.HOSPITAL
            res.medical_degree_flg = r.MEDICAL
            res.tribal_inst_flg = r.TRIBAL
            res.open_to_general_public = r.OPENPUBL
            res.ipeds_participation = r.ACT
            res.merged_inst_id = r.NEWID
            res.ipeds_removal_yr = r.DEATHYR
            res.inst_closed_dt = r.CLOSEDAT
            res.inst_curr_active_flg = r.CYACTIVE
            res.post_secondary_only = r.POSTSEC
            res.post_secondary_flg = r.PSEFLAG
            res.agg_type_flg = r.PSET4FLG
            res.reporting_method = r.RPTMTH
            res.inst_category = r.INSTCAT
            res.carnegie_basic_class_shorthand = r.C15BASIC
            res.carnegie_undergrad_focus = r.C15IPUG
            res.carnegie_grad_focus = r.C15IPGRD
            res.carnegie_undergrad_profile = r.C15UGPRF
            res.carnegie_enrollment_profile = r.C15ENPRF
            res.carnegie_setting_classification = r.C15SZSET
            res.carnegie_basic_classification = r.CCBASIC
            res.carnegie_classification = r.CARNEGIE
            res.land_grant_inst = r.LANDGRNT
            res.inst_size_category = r.INSTSIZE
            res.multi_inst_flg = r.F1SYSTYP
            res.multi_inst_nm = r.F1SYSNAM
            res.multi_inst_id = r.F1SYSCOD
            res.updated_ts = datetime.now()

            session.add(res)

        else:

            record = BaseCollegeBase(
                inst_id=r.UNITID,
                inst_nm=r.INSTNM,
                inst_alias=r.IALIAS,
                chief_admin_nm=r.CHFNM,
                chief_admin_title=r.CHFTITLE,
                general_telephone_num=r.GENTELE,
                ein=r.EIN,
                dun_bradstreet_num=r.DUNS,
                ope_id=r.OPEID,
                ope_title4_flg=r.OPEFLAG,
                url_general=r.WEBADDR,
                url_admissions=r.ADMINURL,
                url_financial_aid=r.FAIDURL,
                url_application=r.APPLURL,
                url_net_price_calculator=r.NPRICURL,
                url_veterans=r.VETURL,
                url_athlete_grad_rate=r.ATHURL,
                url_disability=r.DISAURL,
                inst_sector=r.SECTOR,
                inst_level=r.ICLEVEL,
                inst_control=r.CONTROL,
                level_highest_offering=r.HLOFFER,
                undergrad_offering=r.UGOFFER,
                grad_offering=r.GROFFER,
                degree_highest_offered=r.HDEGOFR1,
                degree_granting_status=r.DEGGRANT,
                hbcu_flg=r.HBCU,
                hospital_flg=r.HOSPITAL,
                medical_degree_flg=r.MEDICAL,
                tribal_inst_flg=r.TRIBAL,
                open_to_general_public=r.OPENPUBL,
                ipeds_participation=r.ACT,
                merged_inst_id=r.NEWID,
                ipeds_removal_yr=r.DEATHYR,
                inst_closed_dt=r.CLOSEDAT,
                inst_curr_active_flg=r.CYACTIVE,
                post_secondary_only=r.POSTSEC,
                post_secondary_flg=r.PSEFLAG,
                agg_type_flg=r.PSET4FLG,
                reporting_method=r.RPTMTH,
                inst_category=r.INSTCAT,
                carnegie_basic_class_shorthand=r.C15BASIC,
                carnegie_undergrad_focus=r.C15IPUG,
                carnegie_grad_focus=r.C15IPGRD,
                carnegie_undergrad_profile=r.C15UGPRF,
                carnegie_enrollment_profile=r.C15ENPRF,
                carnegie_setting_classification=r.C15SZSET,
                carnegie_basic_classification=r.CCBASIC,
                carnegie_classification=r.CARNEGIE,
                land_grant_inst=r.LANDGRNT,
                inst_size_category=r.INSTSIZE,
                multi_inst_flg=r.F1SYSTYP,
                multi_inst_nm=r.F1SYSNAM,
                multi_inst_id=r.F1SYSCOD,
                inserted_ts=datetime.now(),
                updated_ts=datetime.now()
            )

            session.add(record)

    session.commit()
    print("college base processing complete")

