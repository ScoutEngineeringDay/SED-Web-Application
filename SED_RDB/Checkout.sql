CREATE TABLE SED_Database.sedUI_checkout(
	checkout_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
	checkout_title VARCHAR(100),
    checkout_description VARCHAR(200),
    checkout_cost FLOAT UNSIGNED,
    public_key CHAR(32),
    private_key CHAR(32));