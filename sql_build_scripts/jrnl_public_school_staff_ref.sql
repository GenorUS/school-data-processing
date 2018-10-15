/* 
author: Fraser Torning
create date: 10/14/18 
source url: https://nces.ed.gov/ccd/pubschuniv.asp
*/

create table {}.jrnl_pub_school_staff_ref (
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
	FTE FLOAT COMMENT 'Classroom teachers. Total full-time-equivalent classroom teachers. Full-time equivalency reported to the nearest hundredth; field includes two explicit decimal places.',
  INSERTED_TS TIMESTAMP NOT NULL,
  UPDATED_TS TIMESTAMP NOT NULL,

  primary key (NCESSCH),
  index (NCESSCH)
);