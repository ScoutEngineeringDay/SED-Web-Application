/*-- DROP DATABASE IF EXISTS sed_database_test;
-- CREATE DATABASE sed_database_test;

#Generate the Table
-- DROP TABLE IF EXISTS sed_database_test.sedUI_scout;
-- CREATE TABLE sed_database_test.sedUI_scout (
--     scout_id INT UNSIGNED NOT "" AUTO_INCREMENT PRIMARY KEY,
--     first_name VARCHAR(50) NOT "",
--     last_name VARCHAR(50) NOT "",
--     gender ENUM('M', 'F') NOT "",
--     age INT UNSIGNED NOT "",
--     street VARCHAR(50),
--     city VARCHAR(50),
--     state CHAR(2),
--     zip CHAR(5),
--     phone CHAR(13),
--     email VARCHAR(50),
--     emergency_firstname VARCHAR(50),
--     emergency_lastname VARCHAR(50),
--     emergency_phone VARCHAR(50),
--     affiliation ENUM('BSA', 'GSA', 'VentureCrew') NOT "",
--     scout_username VARCHAR(50),
--     scout_password VARCHAR(50)
-- );
-- -- DROP TABLE IF EXISTS sed_database_test.sedUI_health;
-- -- CREATE TABLE sed_database_test.sedUI_health(
-- -- 	scout_id INT UNSIGNED NOT "",
-- --     health_type ENUM('M','A') NOT "",
-- --     health_condition VARCHAR(500),
-- --     description VARCHAR(500),
-- --     FOREIGN KEY fk_scout(scout_id)
-- --     REFERENCES sed_database_test.scout(scout_id) 
-- --     ON UPDATE CASCADE 
-- --     ON DELETE RESTRICT
-- -- );
-- -- DROP TABLE IF EXISTS sed_database_test.sedUI_question_list;
-- -- CREATE TABLE sed_database_test.sedUI_question_list(
-- -- 	question_id INT UNSIGNED NOT "" AUTO_INCREMENT PRIMARY KEY,
-- --     question VARCHAR(100)
-- -- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_staff;
-- CREATE TABLE sed_database_test.sedUI_staff(
-- 	staff_id INT UNSIGNED NOT "" AUTO_INCREMENT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     staff_type ENUM('I', 'C'),
--     phone CHAR(13),
--     email VARCHAR(50),
--     street VARCHAR(50), 
--     city VARCHAR(50),
--     state CHAR(2),
--     zip CHAR(5),
--     activity_status ENUM('INA', 'A') NOT ""
-- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_course;
-- CREATE TABLE sed_database_test.sedUI_course(
-- 	class_id INT UNSIGNED NOT "" AUTO_INCREMENT PRIMARY KEY,
--     class_name VARCHAR(50),
--     class_description VARCHAR(500)
-- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_location;
-- CREATE TABLE sed_database_test.sedUI_location(
-- 	location_id INT UNSIGNED NOT "" AUTO_INCREMENT PRIMARY KEY,
--     street VARCHAR(50), 
--     city VARCHAR(50),
--     state CHAR(2),
--     zip CHAR(5),
--     building VARCHAR(50),
--     room_number VARCHAR(10),
--     capacity INT UNSIGNED NOT ""
-- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_workshop;
-- CREATE TABLE sed_database_test.sedUI_workshop(
-- 	workshop_id INT UNSIGNED NOT "" PRIMARY KEY,
--     class_id INT UNSIGNED NOT "",
--     location_id INT UNSIGNED NOT "",
--     workshop_format ENUM('AM','PM','FULL') NOT "",
--     price decimal(5,2) NOT "",
-- 	FOREIGN KEY fk_class(class_id)
--     REFERENCES sed_database_test.class(class_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT,
--     FOREIGN KEY fk_location(location_id)
--     REFERENCES sed_database_test.location(location_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT
-- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_group_staff;
-- CREATE TABLE sed_database_test.sedUI_group_staff(
-- 	workshop_id INT UNSIGNED NOT "",
--     staff_id INT UNSIGNED NOT "",
--     group_name VARCHAR(50),
--     FOREIGN KEY fk_staff(staff_id)
--     REFERENCES sed_database_test.staff(staff_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT,
--     FOREIGN KEY fk_workshop(workshop_id)
--     REFERENCES sed_database_test.workshop(workshop_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT
-- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_security_question;
-- CREATE TABLE sed_database_test.sedUI_security_question(
-- 	scout_id INT UNSIGNED NOT "",
--     question_id INT UNSIGNED NOT "",
--     answer VARCHAR(50),
--     FOREIGN KEY scout_fk(scout_id)
--     REFERENCES sed_database_test.scout(scout_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT,
--     FOREIGN KEY fk_question_list(question_id)
--     REFERENCES sed_database_test.question_list(question_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT
-- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_registration;
-- CREATE TABLE sed_database_test.sedUI_registration(
-- 	scout_id INT UNSIGNED NOT "",
--     workshop_id INT UNSIGNED NOT "",
--     payment_method ENUM('CREDIT', 'DEBIT', 'CHECK', 'CASH'),
--     confirmation_number char(20),					/*NOT SURE WHAT THE FORMATION FOR CONFIRMATION NUMBER IS GOING TO LOOK LIKE HERE*/
--     registration_date DATE,
-- 	FOREIGN KEY scout_fk2(scout_id)
--     REFERENCES sed_database_test.scout(scout_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT,
--     FOREIGN KEY workshop_fk2(workshop_id)
--     REFERENCES sed_database_test.workshop(workshop_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT
-- );
-- DROP TABLE IF EXISTS sed_database_test.sedUI_workshop_session;
-- CREATE TABLE sed_database_test.sedUI_workshop_session(
-- 	scout_id INT UNSIGNED NOT "",
--     workshop_id INT UNSIGNED NOT "",
--     check_in TIMESTAMP,
--     check_out TIMESTAMP,
--     completion_status ENUM('COMPLETE','INCOMPLETE','HOLD'),
--     FOREIGN KEY scout_fk3(scout_id)
--     REFERENCES sed_database_test.scout(scout_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT,
--     FOREIGN KEY workshop_fk3(workshop_id)
--     REFERENCES sed_database_test.workshop(workshop_id) 
--     ON UPDATE CASCADE 
--     ON DELETE RESTRICT
-- );

#importing testing Data
-- INSERT INTO sed_database_test.sedUI_question_list
-- 	(question_id, question)
-- VALUES
-- 	(1,"What is your mother maiden name?"),
-- 	(2,"What is the name of first pet?"),
-- 	(3,"What is your favorite color?"),
-- 	(4,"What city were you born in?"),
-- 	(5,"Who was your childhood hero?");*/



/*INSERT INTO sed_database_test.sedUI_scout
	(scout_id, first_name, last_name, gender, age, street, city, state, zip_code, phone_number, email, emergency_first_name, emergency_last_name, emergency_phone, affiliation)
VALUES
	(1,"Nicole","Stevens",'F',10,"157 Mitchell Parkway","Brooksville","Fl","34605","3523337677","hmccoy0@surveymonkey.com","Heather","Mccoy","9372327522","GSA"),
	(2,"Carlos","Lawrence",'M',16,"40 Kim Parkway","Hialeah","Fl","33018","7868537745","khansen1@chicagotribune.com","Kenneth","Hansen","9196195355","BSA"),
	(3,"Robert","Jenkins",'M',15,"7 Kennedy Parkway","Midland","Mi","48670","9897879641","nscott2@goodreads.com","Nicholas","Scott","9182850410","BSA"),
	(4,"Stephen","Edwards",'M',18,"5 American Ash Hill","Oakland","Ca","94605","5107469155","tshaw3@oaic.gov.au","Terry","Shaw","5153270752","BSA"),
	(5,"Terry","Scott",'M',19,"36696 Center Way","Cincinnati","Oh","45249","5135888088","jbradley4@vistaprint.com","Jonathan","Bradley","5045577441","BSA"),
	(6,"Terry","Richardson",'M',20,"95 Blackbird Road","Montgomery","Al","36195","3346502871","acollins5@tamu.edu","Adam","Collins","9526439012","BSA"),
	(7,"Ernest","Ross",'M',21,"55754 Maple Drive","Topeka","Ka","66642","7852640379","mfields6@dot.gov","Michael","Fields","6781321200","BSA"),
	(8,"Henry","Fields",'M',23,"950 Express Place","Atlanta","Ge","30316","4047992121","psimmons7@samsung.com","Paul","Simmons","9153058475","BSA"),
	(9,"Justin","Campbell",'M',24,"035 Merchant Crossing","Wilmington","De","19805","3021188055","hallen8@networksolutions.com","Henry","Allen","2161154930","BSA"),
	(10,"Arthur","Murphy",'M',25,"61618 Shopko Center","Glendale","Ar","85305","6234254546","awoods9@google.com.au","Albert","Woods","5167205041","BSA"),
	(11,"Ann","Cole",'F',14,"31298 Springs Street","Longview","Te","75605","9036733863","adiaza@bing.com","Ann","Diaz","4782752782","GSA"),
	(12,"Carolyn","Price",'F',16,"97 Kipling Terrace","Santa Barbara","Ca","93150","8055239426","vharrisonb@sonet.ne.jp","Virginia","Harrison","2395586652","GSA"),
	(13,"Ryan","Mitchell",'M',17,"785 Lillian Lane","Denver","Co","80209","7208393956","rchavezc@technorati.com","Ryan","Chavez","5123164857","BSA"),
	(14,"Jerry","Henry",'M',11,"7054 Rockefeller Park","Harrisburg","Pe","17105","7174272299","gwilliamsd@yahoo.com","Gregory","Williams","4807974539","BSA"),
	(15,"Justin","Bailey",'M',23,"2 Nova Terrace","New Castle","Pe","16107","7242885476","jwelche@si.edu","Jason","Welch","5743680637","BSA"),
	(16,"Maria","Phillips",'F',10,"47922 Ramsey Drive","Lawrenceville","Ge","30045","4047681919","mwrightf@google.fr","Mildred","Wright","3014872197","GSA"),
	(17,"Amanda","Richardson",'F',13,"3408 Arizona Alley","Sacramento","Ca","94257","9166198044","jpattersong@nymag.com","Joyce","Patterson","8593898022","GSA"),
	(18,"Barbara","Mccoy",'F',15,"505 Helena Street","Boise","Id","83716","2088390175","wmartinezh@webnode.com","Wanda","Martinez","8046743787","GSA"),
	(19,"Amy","Lynch",'F',9,"4 Schiller Hill","San Francisco","Ca","94110","4158464876","mthompsoni@feedburner.com","Marie","Thompson","9735070040","GSA"),
	(20,"Diane","Garza",'F',7,"428 Johnson Hill","New Orleans","Lo","70124","985281660","srayj@skype.com","Susan","Ray","2067121598","GSA"),
	(21,"Daniel","Dunn",'M',6,"879 Lighthouse Bay Avenue","Sandy","Ut","84093","8016924755","sromerok@apache.org","Steve","Romero","6147785697","BSA"),
	(22,"Joyce","Nguyen",'F',15,"3 Mifflin Street","Saint Augustine","Fl","32092","9049173935","colsonl@noaa.gov","Carolyn","Olson","2193873051","GSA"),
	(23,"Kathleen","Ryan",'F',16,"71 Sommers Point","New Bedford","Ma","02745","5086889972","kdixonm@ifeng.com","Katherine","Dixon","4786288350","GSA"),
	(24,"Betty","Martin",'F',21,"7798 Manitowish Hill","Midland","Mi","48670","9894685767","jmatthewsn@dedecms.com","Julie","Matthews","7043849431","GSA"),
	(25,"Gregory","Wright",'M',15,"13 Service Point","Plano","Te","75074","9725543988","efernandezo@ibm.com","Ernest","Fernandez","8607928732","BSA"),
	(26,"Ralph","West",'M',10,"603 Esker Junction","Oakland","Ca","94611","5109248062","rpattersonp@t.co","Ralph","Patterson","2023536461","BSA"),
	(27,"Clarence","Castillo",'M',11,"21350 Calypso Lane","Tulsa","Ok","74149","9185432653","jfloresq@soundcloud.com","Jeffrey","Flores","8175264055","BSA"),
	(28,"Joyce","Shaw",'F',10,"45 Marquette Place","Norfolk","Va","23551","7575853148","triverar@163.com","Tina","Rivera","4784326569","GSA"),
	(29,"Michael","Mitchell",'M',11,"435 Sycamore Trail","San Diego","Ca","92127","7607570980","jadamss@reference.com","Jose","Adams","2029067625","BSA"),
	(30,"Adam","Washington",'M',12,"45 Kinsman Center","Mobile","Al","36610","2517077494","acampbellt@google.com.au","Anthony","Campbell","2512795035","BSA");*/

-- INSERT INTO sed_database_test.sedUI_health
-- 	(scout_id, health_type, health_condition,description)
-- VALUES
-- 	(1, 'A', "peanut", "carry medicine in white contain, blue cap"),
--     (2, 'M', "broken arm", "ETA heal 20days"),
--     (4, 'A', "seafood", "carry medicine"),
--     (6, 'M', "spine issue", "don't let lift anything over 10lbs");
-- INSERT INTO sed_database_test.sedUI_security_question
-- 	(scout_id, question_id, answer)
-- VALUES
-- 	(1, 5, "Bob Marley"),
--     (2, 2, "Jessie"),
--     (3, 1, "Hendrix"),
--     (4, 2, "Bob Marley"),
--     (5, 2, "Jessie"),
--     (6, 2, "Hendrix"),
--     (7, 2, "Bob Marley"),
--     (8, 2, "Jessie"),
--     (9, 2, "Hendrix"),
--     (10, 2, "Bob Marley"),
--     (11, 2, "Jessie"),
--     (12, 2, "Hendrix"),
--     (13, 2, "Bob Marley"),
--     (14, 2, "Jessie"),
--     (15, 2, "Hendrix"),
--     (16, 2, "Bob Marley"),
--     (17, 2, "Jessie"),
--     (18, 2, "Hendrix"),
--     (19, 2, "Bob Marley"),
--     (20, 2, "Jessie"),
--     (21, 2, "Hendrix"),
--     (22, 2, "Bob Marley"),
--     (23, 2, "Jessie"),
--     (24, 2, "Hendrix"),
--     (25, 2, "Bob Marley"),
--     (26, 2, "Jessie"),
--     (27, 2, "Hendrix"),
--     (28, 2, "Bob Marley"),
--     (29, 2, "Jessie"),
--     (30, 2, "Hendrix");

/*INSERT INTO sed_database_test.sedUI_course 
	(class_id, class_name, class_description)
VALUES
	(1,"Astronomy",""),
    (2,"Aviation",""),
    (3,"Chemistry",""),
    (4,"Composite Materials",""),
    (5,"Drafting",""),
    (6,"Electricity",""),
    (7,"Electronics",""),
    (8,"Energy",""),
    (9,"Engineering",""),
    (10,"Game Design",""),
    (11,"model Design",""),
    (12,"Nuclear Science",""),
    (13,"Oceanography",""),
    (14,"Programming",""),
    (15,"Robotics",""),
    (16,"Space Exploration",""),
    (17,"Sustainability",""),
    (18,"Weather",""),
    (19,"Removed",""),
    (20,"Radio",""),
    (21,"Computers",""),
    (22,"Inventing","");*/

/*INSERT INTO sed_database_test.sedUI_location
	(location_id,street,city,state,zip_code,building,room_number,capacity)
VALUES
	(1,"1959 Sage Trail","Ocala","FL",34474,"Aivee",96,53),
	(2,"42869 Holmberg Point","Bismarck","ND",58505,"Aivee",32,72),
	(3,"5 Merry Plaza","El Paso","TX",79950,"Skidoo",27,94),
	(4,"3 Hazelcrest Place","Tacoma","WA",98424,"Youspan",18,53),
	(5,"7 Village Trail","Bakersfield","CA",93386,"Riffpedia",70,68),
	(6,"5 Manitowish Street","North Little Rock","AR",72199,"Wordware",18,81),
	(7,"96516 Southridge Circle","Oklahoma City","OK",73124,"Feedmix",45,98),
	(8,"396 Veith Avenue","Jamaica","NY",11447,"Trunyx",97,100),
	(9,"32629 Anniversary Parkway","Atlanta","GA",30368,"Browseblab",75,64),
	(10,"25093 Chinook Pass","Little Rock","AR",72222,"Gigabox",77,65),
	(11,"41131 Everett Way","El Paso","TX",88546,"Riffpedia",82,98);*/
INSERT INTO sed_database_test.sedUI_staff
	(staff_id,first_name,last_name,staff_type,phone_number,email,street,city,state,zip_code,activity_status)
VALUES
	(1,"Donna","Burns",'I',"5514471666","dburns0@ifeng.com","29856 Talmadge Plaza","Young America","MN",55557,"A"),
	(2,"Rachel","Bennett",'I',"9171051172","rbennett1@forbes.com","843 Reinke Court","Fresno","CA",93726,"A"),
	(3,"Christina","Austin",'C',"6073904625","caustin2@blogtalkradio.com","97534 Independence Drive","Macon","GA",31296,"A"),
	(4,"Jennifer","Parker",'C',"4947351760","jparker3@hc360.com","5482 Chinook Street","Stamford","CT",06922,"A"),
	(5,"Thomas","Morales",'I',"6053293551","tmorales4@jalbum.net","9 Center Avenue","Tucson","AZ",85720,"A"),
	(6,"Rose","Garza",'C',"2731291519","rgarza5@ox.ac.uk","261 Brown Avenue","Las Vegas","NV",89178,"A"),
	(7,"Wanda","Hamilton",'I',"4801622865","whamilton6@hibu.com","0 Butterfield Pass","Harrisburg","PA",17110,"A"),
	(8,"Clarence","Carroll",'C',"1815013018","ccarroll7@go.com","63 Summit Plaza","Albany","NY",12232,"A"),
	(9,"Martin","Riley",'C',"5136044083","mriley8@google.co.uk","82 Florence Junction","San Rafael","CA",94913,"A"),
	(10,"Christina","Clark",'I',"7452494625","cclark9@quantcast.com","92781 Debs Way","Huntsville","AL",35815,"A");
-- INSERT INTO sed_database_test.sedUI_workshop
-- 	(workshop_id, class_id, location_id, workshop_format, price)
-- VALUES
-- 	(1,3,4,"PM",11.61),
-- 	(2,7,4,"AM",28.25),
-- 	(3,1,5,"AM",24.25),
-- 	(4,5,4,"PM",18.62),
-- 	(5,4,5,"AM",29.12),
-- 	(6,4,3,"PM",28.16),
-- 	(7,7,2,"AM",25.88),
-- 	(8,3,3,"PM",20.83),
-- 	(9,7,2,"AM",14.43),
-- 	(10,6,5,"AM",13.07);