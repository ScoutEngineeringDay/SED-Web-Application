DROP DATABASE IF EXISTS sed_database;
CREATE DATABASE sed_database;

#Generate the Table
CREATE TABLE sed_database.sedUI_scout (
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
CREATE TABLE sed_database.sedUI_health(
	scout_id INT UNSIGNED NOT NULL,
    health_type ENUM('M','A') NOT NULL,
    health_condition VARCHAR(500),
    description VARCHAR(500),
    FOREIGN KEY fk_scout(scout_id)
    REFERENCES sed_database.scout(scout_id) 
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);
CREATE TABLE sed_database.sedUI_question_list(
	question_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(100)
);
CREATE TABLE sed_database.sedUI_staff(
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
CREATE TABLE sed_database.sedUI_class(
	class_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50),
    class_description VARCHAR(500)
);
CREATE TABLE sed_database.sedUI_location(
	location_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(50), 
    city VARCHAR(50),
    state CHAR(2),
    zip CHAR(5),
    building VARCHAR(50),
    room_number VARCHAR(10),
    capacity INT UNSIGNED NOT NULL
);
CREATE TABLE sed_database.sedUI_workshop(
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
CREATE TABLE sed_database.sedUI_group_staff(
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
CREATE TABLE sed_database.sedUI_security_question(
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
CREATE TABLE sed_database.sedUI_registration(
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
CREATE TABLE sed_database.sedUI_workshop_session(
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

#importing testing Data
INSERT INTO sed_database.sedUI_question_list
	(question_id, question)
VALUES
	(1,"What is your mother maiden name?"),
	(2,"What is the name of first pet?"),
	(3,"What is your favorite color?"),
	(4,"What city were you born in?"),
	(5,"Who was your childhood hero?");
INSERT INTO sed_database.sedUI_scout
	(scout_id, first_name, last_name, gender, age, street, city, state, zip, phone, email, emergency_firstname, emergency_lastname, emergency_phone, affiliation, scout_username, scout_password)
VALUES
	(1,"Nicole","Stevens",'F',10,"157 Mitchell Parkway","Brooksville","Fl","34605","(352)333-7677","hmccoy0@surveymonkey.com","Heather","Mccoy","(937)232-7522","GSA","hmccoy0","GtVERXSISQw"),
	(2,"Carlos","Lawrence",'M',16,"40 Kim Parkway","Hialeah","Fl","33018","(786)853-7745","khansen1@chicagotribune.com","Kenneth","Hansen","(919)619-5355","BSA","khansen1","Qo9FzsDyGW7"),
	(3,"Robert","Jenkins",'M',15,"7 Kennedy Parkway","Midland","Mi","48670","(989)787-9641","nscott2@goodreads.com","Nicholas","Scott","(918)285-0410","BSA","nscott2","3zpECF"),
	(4,"Stephen","Edwards",'M',18,"5 American Ash Hill","Oakland","Ca","94605","(510)746-9155","tshaw3@oaic.gov.au","Terry","Shaw","(515)327-0752","BSA","tshaw3","oKvj7LUS5ZS"),
	(5,"Terry","Scott",'M',19,"36696 Center Way","Cincinnati","Oh","45249","(513)588-8088","jbradley4@vistaprint.com","Jonathan","Bradley","(504)557-7441","BSA","jbradley4","R9sPaStxG"),
	(6,"Terry","Richardson",'M',20,"95 Blackbird Road","Montgomery","Al","36195","(334)650-2871","acollins5@tamu.edu","Adam","Collins","(952)643-9012","BSA","acollins5","aPc8l4i2Rmw"),
	(7,"Ernest","Ross",'M',21,"55754 Maple Drive","Topeka","Ka","66642","(785)264-0379","mfields6@dot.gov","Michael","Fields","(678)132-1200","BSA","mfields6","o9xxpXXotbIJ"),
	(8,"Henry","Fields",'M',23,"950 Express Place","Atlanta","Ge","30316","(404)799-2121","psimmons7@samsung.com","Paul","Simmons","(915)305-8475","BSA","psimmons7","MqFLd07hR"),
	(9,"Justin","Campbell",'M',24,"035 Merchant Crossing","Wilmington","De","19805","(302)118-8055","hallen8@networksolutions.com","Henry","Allen","(216)115-4930","BSA","hallen8","ukDWxxES8fkP"),
	(10,"Arthur","Murphy",'M',25,"61618 Shopko Center","Glendale","Ar","85305","(623)425-4546","awoods9@google.com.au","Albert","Woods","(516)720-5041","BSA","awoods9","ozknUfBabs"),
	(11,"Ann","Cole",'F',14,"31298 Springs Street","Longview","Te","75605","(903)673-3863","adiaza@bing.com","Ann","Diaz","(478)275-2782","GSA","adiaza","pO6AGm1"),
	(12,"Carolyn","Price",'F',16,"97 Kipling Terrace","Santa Barbara","Ca","93150","(805)523-9426","vharrisonb@so-net.ne.jp","Virginia","Harrison","(239)558-6652","GSA","vharrisonb","vuX2gaf"),
	(13,"Ryan","Mitchell",'M',17,"785 Lillian Lane","Denver","Co","80209","(720)839-3956","rchavezc@technorati.com","Ryan","Chavez","(512)316-4857","BSA","rchavezc","v9wqjTC1m"),
	(14,"Jerry","Henry",'M',11,"7054 Rockefeller Park","Harrisburg","Pe","17105","(717)427-2299","gwilliamsd@yahoo.com","Gregory","Williams","(480)797-4539","BSA","gwilliamsd","S7GKKSY"),
	(15,"Justin","Bailey",'M',23,"2 Nova Terrace","New Castle","Pe","16107","(724)288-5476","jwelche@si.edu","Jason","Welch","(574)368-0637","BSA","jwelche","NUZabQb"),
	(16,"Maria","Phillips",'F',10,"47922 Ramsey Drive","Lawrenceville","Ge","30045","(404)768-1919","mwrightf@google.fr","Mildred","Wright","(301)487-2197","GSA","mwrightf","bqa0kuI7ug"),
	(17,"Amanda","Richardson",'F',13,"3408 Arizona Alley","Sacramento","Ca","94257","(916)619-8044","jpattersong@nymag.com","Joyce","Patterson","(859)389-8022","GSA","jpattersong","PBnUeDkmJf"),
	(18,"Barbara","Mccoy",'F',15,"505 Helena Street","Boise","Id","83716","(208)839-0175","wmartinezh@webnode.com","Wanda","Martinez","(804)674-3787","GSA","wmartinezh","vgC2F8gfH7"),
	(19,"Amy","Lynch",'F',9,"4 Schiller Hill","San Francisco","Ca","94110","(415)846-4876","mthompsoni@feedburner.com","Marie","Thompson","(973)507-0040","GSA","mthompsoni","FCnjrAloj"),
	(20,"Diane","Garza",'F',7,"428 Johnson Hill","New Orleans","Lo","70124","(985)281660","srayj@skype.com","Susan","Ray","(206)712-1598","GSA","srayj","Q8IJg6KXBX"),
	(21,"Daniel","Dunn",'M',6,"879 Lighthouse Bay Avenue","Sandy","Ut","84093","(801)692-4755","sromerok@apache.org","Steve","Romero","(614)778-5697","BSA","sromerok","DP0sHSWdA"),
	(22,"Joyce","Nguyen",'F',15,"3 Mifflin Street","Saint Augustine","Fl","32092","(904)917-3935","colsonl@noaa.gov","Carolyn","Olson","(219)387-3051","GSA","colsonl","HiebIs8"),
	(23,"Kathleen","Ryan",'F',16,"71 Sommers Point","New Bedford","Ma","02745","(508)688-9972","kdixonm@ifeng.com","Katherine","Dixon","(478)628-8350","GSA","kdixonm","1Yq4FgrnKpo"),
	(24,"Betty","Martin",'F',21,"7798 Manitowish Hill","Midland","Mi","48670","(989)468-5767","jmatthewsn@dedecms.com","Julie","Matthews","(704)384-9431","GSA","jmatthewsn","15z8GJ"),
	(25,"Gregory","Wright",'M',15,"13 Service Point","Plano","Te","75074","(972)554-3988","efernandezo@ibm.com","Ernest","Fernandez","(860)792-8732","BSA","efernandezo","10P1xq7BSrB"),
	(26,"Ralph","West",'M',10,"603 Esker Junction","Oakland","Ca","94611","(510)924-8062","rpattersonp@t.co","Ralph","Patterson","(202)353-6461","BSA","rpattersonp","jDGuRPx"),
	(27,"Clarence","Castillo",'M',11,"21350 Calypso Lane","Tulsa","Ok","74149","(918)543-2653","jfloresq@soundcloud.com","Jeffrey","Flores","(817)526-4055","BSA","jfloresq","G'M'o69jS1"),
	(28,"Joyce","Shaw",'F',10,"45 Marquette Place","Norfolk","Va","23551","(757)585-3148","triverar@163.com","Tina","Rivera","(478)432-6569","GSA","triverar","3qIsYp'M'mkXQ6"),
	(29,"Michael","Mitchell",'M',11,"435 Sycamore Trail","San Diego","Ca","92127","(760)757-0980","jadamss@reference.com","Jose","Adams","(202)906-7625","BSA","jadamss","SVsOQ3kuwCI"),
	(30,"Adam","Washington",'M',12,"45 Kinsman Center","Mobile","Al","36610","(251)707-7494","acampbellt@google.com.au","Anthony","Campbell","(251)279-5035","BSA","acampbellt","jTVFjQX9Gzv8");
INSERT INTO sed_database.sedUI_health
	(scout_id, health_type, health_condition,description)
VALUES
	(1, 'A', "peanut", "carry medicine in white contain, blue cap"),
    (2, 'M', "broken arm", "ETA heal 20days"),
    (4, 'A', "seafood", "carry medicine"),
    (6, 'M', "spine issue", "don't let lift anything over 10lbs");
INSERT INTO sed_database.sedUI_security_question
	(scout_id, question_id, answer)
VALUES
	(1, 5, "Bob Marley"),
    (2, 2, "Jessie"),
    (3, 1, "Hendrix"),
    (4, 2, "Bob Marley"),
    (5, 2, "Jessie"),
    (6, 2, "Hendrix"),
    (7, 2, "Bob Marley"),
    (8, 2, "Jessie"),
    (9, 2, "Hendrix"),
    (10, 2, "Bob Marley"),
    (11, 2, "Jessie"),
    (12, 2, "Hendrix"),
    (13, 2, "Bob Marley"),
    (14, 2, "Jessie"),
    (15, 2, "Hendrix"),
    (16, 2, "Bob Marley"),
    (17, 2, "Jessie"),
    (18, 2, "Hendrix"),
    (19, 2, "Bob Marley"),
    (20, 2, "Jessie"),
    (21, 2, "Hendrix"),
    (22, 2, "Bob Marley"),
    (23, 2, "Jessie"),
    (24, 2, "Hendrix"),
    (25, 2, "Bob Marley"),
    (26, 2, "Jessie"),
    (27, 2, "Hendrix"),
    (28, 2, "Bob Marley"),
    (29, 2, "Jessie"),
    (30, 2, "Hendrix");
INSERT INTO sed_database.sedUI_class 
	(class_id, class_name, class_description)
VALUES
	(1,"Astronomy",null),
    (2,"Aviation",null),
    (3,"Chemistry",null),
    (4,"Composite Materials",null),
    (5,"Drafting",null),
    (6,"Electricity",null),
    (7,"Electronics",null),
    (8,"Energy",null),
    (9,"Engineering",null),
    (10,"Game Design",null),
    (11,"model Design",null),
    (12,"Nuclear Science",null),
    (13,"Oceanography",null),
    (14,"Programming",null),
    (15,"Robotics",null),
    (16,"Space Exploration",null),
    (17,"Sustainability",null),
    (18,"Weather",null),
    (19,"Removed",null),
    (20,"Radio",null),
    (21,"Computers",null),
    (22,"Inventing",null);
INSERT INTO sed_database.sedUI_location
	(location_id,street,city,state,zip,building,room_number,capacity)
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
	(11,"41131 Everett Way","El Paso","TX",88546,"Riffpedia",82,98);
INSERT INTO sed_database.sedUI_staff
	(staff_id,first_name,last_name,staff_type,phone,email,street,city,state,zip,activity_status)
VALUES
	(1,"Donna","Burns",'I',"(551)447-1666","dburns0@ifeng.com","29856 Talmadge Plaza","Young America","MN",55557,"ACTIVE"),
	(2,"Rachel","Bennett",'I',"(917)105-1172","rbennett1@forbes.com","843 Reinke Court","Fresno","CA",93726,"ACTIVE"),
	(3,"Christina","Austin",'C',"(607)390-4625","caustin2@blogtalkradio.com","97534 Independence Drive","Macon","GA",31296,"ACTIVE"),
	(4,"Jennifer","Parker",'C',"(494)735-1760","jparker3@hc360.com","5482 Chinook Street","Stamford","CT",06922,"ACTIVE"),
	(5,"Thomas","Morales",'I',"(605)329-3551","tmorales4@jalbum.net","9 Center Avenue","Tucson","AZ",85720,"ACTIVE"),
	(6,"Rose","Garza",'C',"(273)129-1519","rgarza5@ox.ac.uk","261 Brown Avenue","Las Vegas","NV",89178,"ACTIVE"),
	(7,"Wanda","Hamilton",'I',"(480)162-2865","whamilton6@hibu.com","0 Butterfield Pass","Harrisburg","PA",17110,"ACTIVE"),
	(8,"Clarence","Carroll",'C',"(181)501-3018","ccarroll7@go.com","63 Summit Plaza","Albany","NY",12232,"ACTIVE"),
	(9,"Martin","Riley",'C',"(513)604-4083","mriley8@google.co.uk","82 Florence Junction","San Rafael","CA",94913,"ACTIVE"),
	(10,"Christina","Clark",'I',"(745)249-4625","cclark9@quantcast.com","92781 Debs Way","Huntsville","AL",35815,"ACTIVE");
INSERT INTO sed_database.sedUI_workshop
	(workshop_id, class_id, location_id, workshop_format, price)
VALUES
	(1,3,4,"PM",11.61),
	(2,7,4,"AM",28.25),
	(3,1,5,"AM",24.25),
	(4,5,4,"PM",18.62),
	(5,4,5,"AM",29.12),
	(6,4,3,"PM",28.16),
	(7,7,2,"AM",25.88),
	(8,3,3,"PM",20.83),
	(9,7,2,"AM",14.43),
	(10,6,5,"AM",13.07);