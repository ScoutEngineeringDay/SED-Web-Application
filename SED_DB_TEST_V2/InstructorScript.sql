CREATE TABLE SED_Database.sedUI_instructor(
	instructor_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
	instructor_first_name VARCHAR(50) NOT NULL,
	instructor_last_name VARCHAR(50) NOT NULL,
	instructor_phone CHAR(10),
	instructor_email VARCHAR(50) NOT NULL,
    instructor_status ENUM('ACTIVE', 'INACTIVE') NOT NULL
);
INSERT INTO SED_Database.sedUI_instructor
	(instructor_first_name, instructor_last_name, instructor_phone, instructor_email, instructor_status)
VALUES
	("Justin", "Doe", "9999999999", "JustDoe@gmail.com", "ACTIVE"),
	("Jay", "Doe", "9999999999", "JD@gmail.com", "ACTIVE"),
	("Melissa", "Lovely", "9999999999", "MLove@gmail.com", "ACTIVE"),
	("Donna","Burns","5514471666","dburns0@ifeng.com", "ACTIVE"),
	("Rachel","Bennett","9171051172","rbennett1@forbes.com", "ACTIVE"),
	("Christina","Austin","6073904625","caustin2@blogtalkradio.com", "ACTIVE"),
	("Jennifer","Parker","4947351760","jparker3@hc360.com", "ACTIVE"),
	("Thomas","Morales","6053293551","tmorales4@jalbum.net", "ACTIVE"),
	("Rose","Garza","2731291519","rgarza5@ox.ac.uk", "ACTIVE"),
	("Wanda","Hamilton","4801622865","whamilton6@hibu.com", "ACTIVE"),
	("Clarence","Carroll","1815013018","ccarroll7@go.com", "ACTIVE"),
	("Martin","Riley","5136044083","mriley8@google.co.uk", "ACTIVE"),
	("Christina","Clark","7452494625","cclark9@quantcast.com", "ACTIVE");