CREATE TABLE SED_Database.sedUI_mailpayment(
	mailPayment_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
    mailPayment_person VARCHAR(100) NOT NULL,
    mailPayment_building VARCHAR(50) NOT NULL,
    mailPayment_street VARCHAR(50) NOT NULL,
    mailPayment_city VARCHAR(50) NOT NULL,
    mailPayment_state VARCHAR(2) NOT NULL,
    mailPayment_zip VARCHAR(6) NOT NULL,
    mailPayment_due_date VARCHAR(8) NOT NULL
);
