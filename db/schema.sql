DROP DATABASE IF EXISTS sed_database;
CREATE DATABASE sed_database;

CREATE TABLE sed_database.scout (
    scout_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender ENUM('M', 'F') NOT NULL,
    age INT UNSIGNED NOT NULL,
    street VARCHAR(50),
    city VARCHAR(50),
    state CHAR(2),
    zip CHAR(5),
    phone CHAR(13),
    email VARCHAR(50),
    emergency_firstname VARCHAR(50),
    emergency_lastname VARCHAR(50),
    emergency_phone VARCHAR(50),
    affiliation ENUM('BSA', 'GSA', 'VentureCrew') NOT NULL,
    scout_username VARCHAR(50),
    scout_password VARCHAR(50)
);
CREATE TABLE sed_database.health(
	scout_id INT UNSIGNED NOT NULL,
    health_type ENUM('M','A') NOT NULL,
    health_condition VARCHAR(500),
    description VARCHAR(500),
    FOREIGN KEY fk_scout(scout_id)
    REFERENCES sed_database.scout(scout_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);
CREATE TABLE sed_database.question_list(
	question_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(100)
);

CREATE TABLE sed_database.staff(
	staff_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    staff_type ENUM('I', 'C'),
    phone CHAR(13),
    email VARCHAR(50),
    street VARCHAR(50), 
    city VARCHAR(50),
    state CHAR(2),
    zip CHAR(5),
    activity_status ENUM('INACTIVE', 'ACTIVE') NOT NULL
);
CREATE TABLE sed_database.class(
	class_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50),
    class_description VARCHAR(500)
);
CREATE TABLE sed_database.location(
	location_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(50), 
    city VARCHAR(50),
    state CHAR(2),
    zip CHAR(5),
    building VARCHAR(50),
    room_number VARCHAR(10),
    capacity INT UNSIGNED NOT NULL
);
CREATE TABLE sed_database.workshop(
	workshop_id INT UNSIGNED NOT NULL PRIMARY KEY,
    class_id INT UNSIGNED NOT NULL,
    location_id INT UNSIGNED NOT NULL,
    workshop_format ENUM('AM','PM','FULL') NOT NULL,
    price decimal(5,2) NOT NULL,
	FOREIGN KEY fk_class(class_id)
    REFERENCES sed_database.class(class_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT,
    FOREIGN KEY fk_location(location_id)
    REFERENCES sed_database.location(location_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);


CREATE TABLE sed_database.group_staff(
	workshop_id INT UNSIGNED NOT NULL,
    staff_id INT UNSIGNED NOT NULL,
    group_name VARCHAR(50),
    FOREIGN KEY fk_staff(staff_id)
    REFERENCES sed_database.staff(staff_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT,
    FOREIGN KEY fk_workshop(workshop_id)
    REFERENCES sed_database.workshop(workshop_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);
CREATE TABLE sed_database.security_question(
	scout_id INT UNSIGNED NOT NULL,
    question_id INT UNSIGNED NOT NULL,
    answer VARCHAR(50),
    FOREIGN KEY scout_fk(scout_id)
    REFERENCES sed_database.scout(scout_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT,
    FOREIGN KEY fk_question_list(question_id)
    REFERENCES sed_database.question_list(question_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);
CREATE TABLE sed_database.registration(
	scout_id INT UNSIGNED NOT NULL,
    workshop_id INT UNSIGNED NOT NULL,
    payment_method ENUM('CREDIT', 'DEBIT', 'CHECK', 'CASH'),
    confirmation_number char(20),					/*NOT SURE WHAT THE FORMATION FOR CONFIRMATION NUMBER IS GOING TO LOOK LIKE HERE*/
    registration_date DATE,
	FOREIGN KEY scout_fk2(scout_id)
    REFERENCES sed_database.scout(scout_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT,
    FOREIGN KEY workshop_fk2(workshop_id)
    REFERENCES sed_database.workshop(workshop_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);
CREATE TABLE sed_database.workshop_session(
	scout_id INT UNSIGNED NOT NULL,
    workshop_id INT UNSIGNED NOT NULL,
    check_in TIMESTAMP,
    check_out TIMESTAMP,
    completion_status ENUM('COMPLETE','INCOMPLETE','HOLD'),
    FOREIGN KEY scout_fk3(scout_id)
    REFERENCES sed_database.scout(scout_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT,
    FOREIGN KEY workshop_fk3(workshop_id)
    REFERENCES sed_database.workshop(workshop_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);