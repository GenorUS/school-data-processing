/* 
author: Fraser Torning
create date: 10/14/18 
source url: https://nces.ed.gov/ccd/pubschuniv.asp
*/

create table jrnl_pub_school_eligibility_ref (
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
	TOTFRL FLOAT COMMENT 'Total of free lunch eligible and reduced-price lunch eligible. The total is only available if both of the details (or the total) were reported.',
	FRELCH FLOAT COMMENT 'Count of students eligible to participate in the Free Lunch Program under the National School Lunch Act',
	REDLCH FLOAT COMMENT 'Count of students eligible to participate in the Reduced-Price Lunch Program under the National School Lunch Act',
    
    primary key (NCESSCH),
    index (NCESSCH)
);