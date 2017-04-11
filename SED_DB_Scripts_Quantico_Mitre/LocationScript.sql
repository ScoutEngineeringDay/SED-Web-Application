CREATE TABLE SED_Database.sedUI_location(
	location_id INT(5) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
	location_building VARCHAR(50) NOT NULL,
	location_room VARCHAR(10) NOT NULL,
    location_capacity INT
);
INSERT INTO SED_Database.sedUI_location
	(location_building,	location_room, location_capacity)
VALUES
('MITRE2','1N926',20)
,('MITRE2','5N112',20)
,('MITRE2','4N119',20)
,('MITRE4','6J214',20)
,('MITRE4','6J324',20)
,('MITRE2','0N723',20)
,('MITRE2','1N662',20)
,('MITRE4','2J208',20)
,('MITRE4','3J324',20)
,('MITRE2','1N141',20)
,('MITRE2','4N112',20)
,('MITRE2','4N116',20)
,('MITRE2','1N100',20)
,('MITRE2','2N109',20)
,('MITRE2','1N102',20)
,('MITRE4','7J214',20)
,('MITRE2','5N116',20)
,('MITRE4','5J324',20)
,('MITRE4','5J214',20)
,('MITRE4','8J214',20)
,('MITRE4','9J214',20)
,('MITRE4','10J214',20)
,('MITRE4','11J214',20)
,('MITRE2','5N704',20)
,('MITRE2','1N136',20)
,('MITRE2','5N122',20);
