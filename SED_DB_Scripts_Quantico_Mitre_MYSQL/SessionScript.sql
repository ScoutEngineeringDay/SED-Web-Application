CREATE TABLE SED_Database.sedUI_session(
	session_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
  session_year YEAR(4) NOT NULL,
	scout_id INT(10) ZEROFILL NOT NULL,
	payment_method ENUM('Pay_Mail', 'Pay_Online', 'Waived') NOT NULL,
	payment_amount INT UNSIGNED,
  payment_status ENUM('PAID', 'NOT PAID') NOT NULL,
  open_ceremony CHAR(1),
	workshop1_id INT(10) ZEROFILL NOT NULL,
  workshop1_status ENUM('COMPLETE', 'INCOMPLETE', 'IN PROGRESS'),
	workshop2_id INT(10) ZEROFILL,
  workshop2_status ENUM('COMPLETE', 'INCOMPLETE', 'IN PROGRESS'),
	confirmation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	event_checkin TIMESTAMP NULL DEFAULT NULL,
	event_checkout TIMESTAMP NULL DEFAULT NULL,
	workshop1_checkin TIMESTAMP NULL DEFAULT NULL,
	workshop1_checkout TIMESTAMP NULL DEFAULT NULL,
	workshop2_checkin TIMESTAMP NULL DEFAULT NULL,
	workshop2_checkout TIMESTAMP NULL DEFAULT NULL);

INSERT INTO SED_Database.sedUI_session
	(scout_id, session_year, payment_method, payment_amount, payment_status, open_ceremony, workshop1_id, workshop1_status, workshop2_id, workshop2_status)
VALUES
	(1,2017,'Pay_Mail', 40.00,'PAID', 'A', 1,'IN PROGRESS',5, 'IN PROGRESS'),
  (2,2017,'Pay_Mail', 40.00,'PAID', 'A', 1,'IN PROGRESS',5, 'IN PROGRESS');
