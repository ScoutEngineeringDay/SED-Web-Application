CREATE TABLE SED_Database.sedUI_scout(
	scout_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
    confirmation_id CHAR(32) NOT NULL,
	scout_first_name VARCHAR(50) NOT NULL,
	scout_last_name VARCHAR(50) NOT NULL,
	scout_phone CHAR(13),
	scout_email VARCHAR(50) NOT NULL,
	scout_photo BOOLEAN NOT NULL DEFAULT 0,
	scout_medical VARCHAR(5000),
	scout_allergy VARCHAR(5000),
	scout_type ENUM('BOY', 'GIRL', 'OTHER') NOT NULL,
	unit_number VARCHAR(20) NOT NULL,
	emergency_first_name VARCHAR(50) NOT NULL,
	emergency_last_name VARCHAR(50) NOT NULL,
	emergency_phone CHAR(13) NOT NULL,
	emergency_email VARCHAR(50) NOT NULL,
    scout_status ENUM('EVENT_CHECKIN','WORKSHOP1_CHECKIN','WORKSHOP1_CHECKOUT','WORKSHOP2_CHECKIN','WORKSHOP2_CHECKOUT','EVENT_CHECKOUT', 'UNDERWAY') DEFAULT 'UNDERWAY' NOT NULL,
    scout_year YEAR(4) NOT NULL
);
