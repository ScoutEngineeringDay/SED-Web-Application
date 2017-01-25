CREATE TABLE SED_Database.sedUI_scout2(
	scout_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
	scout_first_name VARCHAR(50) NOT NULL,
	scout_last_name VARCHAR(50) NOT NULL,
	scout_phone CHAR(13),
	scout_email VARCHAR(50) NOT NULL,
	scout_photo BOOLEAN NOT NULL DEFAULT 0,
	scout_medical VARCHAR(5000),
	scout_allergy VARCHAR(5000),
	scout_food ENUM('MEAL_PLAN1', 'MEAL_PLAN2', 'PACKED') NOT NULL,
	organization ENUM('BSA', 'GSA', 'OTHERS') NOT NULL,
	troop_number VARCHAR(20) NOT NULL,
	emergency_first_name VARCHAR(50) NOT NULL,
	emergency_last_name VARCHAR(50) NOT NULL,
	emergency_phone CHAR(13) NOT NULL,
	emergency_email VARCHAR(50) NOT NULL
);
