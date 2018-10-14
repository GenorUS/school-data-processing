/* 
author: Fraser Torning
create date: 10/14/18 
source url: https://nces.ed.gov/ccd/pubschuniv.asp
*/

create table jrnl_public_school_def (
	school_year char(9) comment 'Year corresponding to survey record',
	FIPST char(2) comment 'American National Standards Institute (ANSI) state code',
	STATENAME varchar(44) comment 'State name',
	ST varchar(2) comment 'State name',
	SCH_NAME varchar(60) comment 'School name',
	LEA_NAME varchar(60) comment 'Education Agency Name',
    STATE_AGENCY_NO varchar(3) comment 'Identifier of the reporting state agency',
	`UNION` varchar(3) comment 'Supervisory Union (SU) Identification Number. For SU administrative centers and component agencies, this is assigned by the state. If the agency is a county superintendent, this is the ANSI county number. If not reported, the field is null',
 	ST_LEAID varchar(35) comment 'State Local Education Number. State’s own ID for the education agency',
	LEAID varchar(7) comment 'NCES Agency Identification Number',
	ST_SCHID varchar(45) comment 'State school identifier',
	NCESSCH varchar(12) comment 'School Identifier (NCES)',
	SCHID varchar(7) comment 'Unique school ID',
	MSTREET1 varchar(30) comment 'Mailing address; street 1',
	MSTREET2 varchar(30) comment 'Mailing address; street 2',
	MSTREET3 varchar(30) comment 'Mailing address; street 3',
	MCITY varchar(30) comment 'Mailing city',
	MSTATE varchar(2) comment 'Mailing state. Two-letter U.S. Postal Service abbreviation of the state where the mailing address is located',
	MZIP varchar(5) comment 'Mailing 5 digit ZIP code',
	MZIP4 varchar(4) comment 'Mailing Secondary ZIP code',
	LSTREET1 varchar(30) comment 'Location address; street 1',
	LSTREET2 varchar(30) comment 'Location address; street 2',
	LSTREET3 varchar(30) comment 'Location address; street 3',
	LCITY varchar(30) comment 'Location city',
	LSTATE varchar(2) comment 'Location state. Two-letter U.S. Postal Service abbreviation',
	LZIP varchar(5) comment 'Location 5 digit ZIP code',
	LZIP4 varchar(4) comment 'Location Secondary ZIP code',
	PHONE varchar(13) comment 'Telephone number',
	WEBSITE varchar(80) comment 'The Uniform Resource Locator (URL) for the unique address of a Web Page of an education entity',
	SY_STATUS varchar(1) comment 'Start of year Status (code)',
	SY_STATUS_TEXT varchar(16) comment 'Start of year Status (description)',
	UPDATED_STATUS varchar(1) comment 'Updated status (code)',
    UPDATED_STATUS_TEXT varchar(16) comment 'Updated status (description)',
	EFFECTIVE_DATE varchar(20) comment 'Effective date of updated status',
	SCH_TYPE varchar(1) comment 'School type (code)',
	SCH_TYPE_TEXT varchar(28) comment 'School type (description)',
	RECON_STATUS varchar(3) comment 'Reconstituted flag',
	OUT_OF_STATE_FLAG varchar(3) comment 'Mailing or Location address is in another state',
	CHARTER_TEXT varchar(14) comment 'Whether a Charter school',
	CHARTAUTH1 varchar(60) comment 'Charter authorizer name (1)',
	CHARTAUTHN1 varchar(14) comment 'Charter authorizer state ID (1). The identifier assigned to the primary public charter school authorizing agency by the SEA.',
	CHARTAUTH2 varchar(60) comment 'Charter authorizer name (2)',
	CHARTAUTHN2 varchar(14) comment 'Charter authorizer state ID (2). The identifier assigned to the primary public charter school authorizing agency by the SEA.',
	NOGRADES varchar(12) comment 'No grades offered',
	G_PK_OFFERED varchar(12) comment 'PK Grade Offered',
	G_KG_OFFERED varchar(12) comment 'KG Grade Offered',
	G_1_OFFERED varchar(12) comment 'Grade 01 Offered',
	G_2_OFFERED varchar(12) comment 'Grade 02 Offered',
	G_3_OFFERED varchar(12) comment 'Grade 03 Offered',
	G_4_OFFERED varchar(12) comment 'Grade 04 Offered',
	G_5_OFFERED varchar(12) comment 'Grade 05 Offered',
	G_6_OFFERED varchar(12) comment 'Grade 06 Offered',
	G_7_OFFERED varchar(12) comment 'Grade 07 Offered',
	G_8_OFFERED varchar(12) comment 'Grade 08 Offered',
	G_9_OFFERED varchar(12) comment 'Grade 09 Offered',
	G_10_OFFERED varchar(12) comment 'Grade 10 Offered',
	G_11_OFFERED varchar(12) comment 'Grade 11 Offered',
	G_12_OFFERED varchar(12) comment 'Grade 12 Offered',
	G_13_OFFERED varchar(12) comment 'Grade 13 Offered',
	G_UG_OFFERED varchar(12) comment 'UG Grade offered',
	G_AE_OFFERED varchar(12) comment 'Adult education offered',
	GSLO varchar(2) comment 'Grades Offered - Lowest',
	GSHI varchar(2) comment 'Grades Offered - Highest',
	`LEVEL` varchar(16) comment 'LEA or school level',
	IGOFFERED varchar(14) comment 'Whether any grades-offered field was adjusted',
    
    primary key (NCESSCH),
    index (NCESSCH),
    index (`LEVEL`),
    index (LSTATE),
    index (LZIP),
    index (LCITY)
);
