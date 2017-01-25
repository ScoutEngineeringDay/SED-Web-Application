CREATE TABLE SED_Database.sedUI_volunteer2(
	volunteer_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
	volunteer_first_name VARCHAR(50) NOT NULL,
	volunteer_last_name VARCHAR(50) NOT NULL,
	volunteer_phone CHAR(10),
	volunteer_email VARCHAR(50) NOT NULL,
	volunteer_area VARCHAR(5000),
    volunteer_status ENUM('ACTIVE', 'INACTIVE') NOT NULL
);
INSERT INTO SED_Database.sedUI_volunteer2
	(volunteer_first_name, volunteer_last_name, volunteer_phone, volunteer_email, volunteer_area, volunteer_status)
VALUES
	("Jane", "Doe", "7033003998","JDoe@gmail.com", "food preparer", "ACTIVE"),
	("Jake", "Doe", "7033003998","justBake@gmail.com", "food preparer", "ACTIVE"),
	("James", "Doe", "7033003998","MI007@gmail.com", "food preparer", "ACTIVE");