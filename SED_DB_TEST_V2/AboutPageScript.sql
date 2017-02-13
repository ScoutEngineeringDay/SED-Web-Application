CREATE TABLE SED_Database.sedUI_aboutpage(
	aboutpage_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
    saveDate VARCHAR(1000),
    eventLocation VARCHAR(1000),
    registrationOpenDate VARCHAR(1000),
    registrationOpenTime VARCHAR(1000),
    locationMap VARCHAR(1000)
);
INSERT INTO SED_Database.sedUI_aboutpage
	(saveDate, eventLocation, registrationOpenDate, registrationOpenTime, locationMap)
VALUES
	("Saturday, March 12, 2016", "McLean, Virginia", "Wednesday, January 20, 2016", "7:00pm", "7515 Colshire Dr, McLean, VA 22102");
