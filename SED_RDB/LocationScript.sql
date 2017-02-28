CREATE TABLE SED_Database.sedUI_location(
	location_id INT(5) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
	location_building VARCHAR(50) NOT NULL,
	location_room VARCHAR(10) NOT NULL,
    location_capacity INT
);
INSERT INTO SED_Database.sedUI_location
	(location_building,	location_room, location_capacity)
VALUES
	("MITRE1", "1a", 20),
	("MITRE2", "2a", 20),
	("MITRE4", "101",20);