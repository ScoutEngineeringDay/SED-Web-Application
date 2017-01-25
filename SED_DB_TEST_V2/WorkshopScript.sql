CREATE TABLE SED_Database.sedUI_workshop2(
	workshop_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
	course_id INT(10) ZEROFILL NOT NULL,
	location_id INT(10) ZEROFILL NOT NULL,
    workshop_time ENUM('AM','PM','FULL') NOT NULL,
    workshop_open TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
INSERT INTO SED_Database.sedUI_workshop2
	(course_id, workshop_time, location_id)
VALUES
	(1,"AM",1),
	(6,"AM",1),
	(3,"AM",2),
	(8,"AM",1),
	(3,"AM",3);