/* 
author: Fraser Torning
create date: 10/14/18 
source url: https://nces.ed.gov/ccd/pubschuniv.asp
*/

create table jrnl_pub_school_characteristics_ref (
	SURVYEAR VARCHAR(9) COMMENT 'Year corresponding to survey record',
	FIPST VARCHAR(2) COMMENT 'American National Standards Institute (ANSI) state code',
	STABR VARCHAR(2) COMMENT 'Postal state abbreviation code',
	STATENAME VARCHAR(44) COMMENT 'State name',
	SEANAME VARCHAR(59) COMMENT 'Name of state education agency',
	LEAID VARCHAR(7) COMMENT 'NCES Agency Identification Number',
	ST_LEAID VARCHAR(35) COMMENT 'State Local Education Number. State\'s own ID for the education agency.',
	LEA_NAME VARCHAR(60) COMMENT 'Education Agency Name',
	SCHID VARCHAR(5) COMMENT 'NCES school identifier',
	ST_SCHID VARCHAR(45) COMMENT 'State school identifier',
	NCESSCH VARCHAR(12) COMMENT 'Unique school ID',
	SCH_NAME VARCHAR(60) COMMENT 'School name',
	TITLEI_TEXT VARCHAR(63) COMMENT 'Title I status (description)',
	TITLEI_STATUS VARCHAR(2) COMMENT 'Title I status (code)',
	TITLEI VARCHAR(14) COMMENT 'Title I Eligible School. This flag indicates whether a school is eligible for participation in either TAS or SWP program authorized by Title I of Public Law 103-382. ',
	STITLEI VARCHAR(14) COMMENT 'School-wide Title I. This flag indicates whether a school is eligible for participation in Schoolwide program authorized by Title I of Public Law 103-382. ',
	SHARED_TIME VARCHAR(7) COMMENT 'Shared Time Indicator',
	MAGNET_TEXT VARCHAR(14) COMMENT 'Magnet School Indicator',
	NSLPSTATUS_TEXT VARCHAR(57) COMMENT 'National School Lunch Program (NSLP) Status (description). Represents the National School Lunch Program (NSLP) Status for the school. ',
	NSLPSTATUS_CODE VARCHAR(3) COMMENT 'National School Lunch Program (NSLP) Status (code). Represents the National School Lunch Program (NSLP) Status for the school. ',
    
    primary key (NCESSCH),
    index (NCESSCH)
);