CREATE TABLE SED_Database.sedUI_aboutpage(
	aboutpage_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
    saveDate VARCHAR(5000),
    eventLocation VARCHAR(5000),
    registrationOpenDate VARCHAR(5000),
    registrationOpenTime VARCHAR(5000),
    locationMap VARCHAR(5000),
    forceClosed BOOLEAN
);
INSERT INTO SED_Database.sedUI_aboutpage
	(saveDate, eventLocation, registrationOpenDate, registrationOpenTime, locationMap)
VALUES
	("Saturday, March 12, 2016", "McLean, Virginia", "Wednesday, January 20, 2016", "7:00pm", "7515 Colshire Dr, McLean, VA 22102");