DROP TABLE IF EXISTS SED_Database.sedUI_scout;
CREATE TABLE SED_Database.sedUI_scout (
    scout_id INT(5) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
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
INSERT INTO sedUI_scout
	(first_name, last_name, gender, age, street, city, state, zip_code, phone_number, email, emergency_first_name, emergency_last_name, emergency_phone, affiliation)
VALUES
	("Nicole","Stevens",'F',10,"157 Mitchell Parkway","Brooksville","Fl","34605","3523337677","hmccoy0@surveymonkey.com","Heather","Mccoy","9372327522","GSA"),
	("Carlos","Lawrence",'M',16,"40 Kim Parkway","Hialeah","Fl","33018","7868537745","khansen1@chicagotribune.com","Kenneth","Hansen","9196195355","BSA"),
	("Robert","Jenkins",'M',15,"7 Kennedy Parkway","Midland","Mi","48670","9897879641","nscott2@goodreads.com","Nicholas","Scott","9182850410","BSA"),
	("Stephen","Edwards",'M',18,"5 American Ash Hill","Oakland","Ca","94605","5107469155","tshaw3@oaic.gov.au","Terry","Shaw","5153270752","BSA"),
	("Terry","Scott",'M',19,"36696 Center Way","Cincinnati","Oh","45249","5135888088","jbradley4@vistaprint.com","Jonathan","Bradley","5045577441","BSA"),
	("Terry","Richardson",'M',20,"95 Blackbird Road","Montgomery","Al","36195","3346502871","acollins5@tamu.edu","Adam","Collins","9526439012","BSA"),
	("Ernest","Ross",'M',21,"55754 Maple Drive","Topeka","Ka","66642","7852640379","mfields6@dot.gov","Michael","Fields","6781321200","BSA"),
	("Henry","Fields",'M',23,"950 Express Place","Atlanta","Ge","30316","4047992121","psimmons7@samsung.com","Paul","Simmons","9153058475","BSA"),
	("Justin","Campbell",'M',24,"035 Merchant Crossing","Wilmington","De","19805","3021188055","hallen8@networksolutions.com","Henry","Allen","2161154930","BSA"),
	("Arthur","Murphy",'M',25,"61618 Shopko Center","Glendale","Ar","85305","6234254546","awoods9@google.com.au","Albert","Woods","5167205041","BSA"),
	("Ann","Cole",'F',14,"31298 Springs Street","Longview","Te","75605","9036733863","adiaza@bing.com","Ann","Diaz","4782752782","GSA"),
	("Carolyn","Price",'F',16,"97 Kipling Terrace","Santa Barbara","Ca","93150","8055239426","vharrisonb@sonet.ne.jp","Virginia","Harrison","2395586652","GSA"),
	("Ryan","Mitchell",'M',17,"785 Lillian Lane","Denver","Co","80209","7208393956","rchavezc@technorati.com","Ryan","Chavez","5123164857","BSA"),
	("Jerry","Henry",'M',11,"7054 Rockefeller Park","Harrisburg","Pe","17105","7174272299","gwilliamsd@yahoo.com","Gregory","Williams","4807974539","BSA"),
	("Justin","Bailey",'M',23,"2 Nova Terrace","New Castle","Pe","16107","7242885476","jwelche@si.edu","Jason","Welch","5743680637","BSA"),
	("Maria","Phillips",'F',10,"47922 Ramsey Drive","Lawrenceville","Ge","30045","4047681919","mwrightf@google.fr","Mildred","Wright","3014872197","GSA"),
	("Amanda","Richardson",'F',13,"3408 Arizona Alley","Sacramento","Ca","94257","9166198044","jpattersong@nymag.com","Joyce","Patterson","8593898022","GSA"),
	("Barbara","Mccoy",'F',15,"505 Helena Street","Boise","Id","83716","2088390175","wmartinezh@webnode.com","Wanda","Martinez","8046743787","GSA"),
	("Amy","Lynch",'F',9,"4 Schiller Hill","San Francisco","Ca","94110","4158464876","mthompsoni@feedburner.com","Marie","Thompson","9735070040","GSA"),
	("Diane","Garza",'F',7,"428 Johnson Hill","New Orleans","Lo","70124","985281660","srayj@skype.com","Susan","Ray","2067121598","GSA"),
	("Daniel","Dunn",'M',6,"879 Lighthouse Bay Avenue","Sandy","Ut","84093","8016924755","sromerok@apache.org","Steve","Romero","6147785697","BSA"),
	("Joyce","Nguyen",'F',15,"3 Mifflin Street","Saint Augustine","Fl","32092","9049173935","colsonl@noaa.gov","Carolyn","Olson","2193873051","GSA"),
	("Kathleen","Ryan",'F',16,"71 Sommers Point","New Bedford","Ma","02745","5086889972","kdixonm@ifeng.com","Katherine","Dixon","4786288350","GSA"),
	("Betty","Martin",'F',21,"7798 Manitowish Hill","Midland","Mi","48670","9894685767","jmatthewsn@dedecms.com","Julie","Matthews","7043849431","GSA"),
	("Gregory","Wright",'M',15,"13 Service Point","Plano","Te","75074","9725543988","efernandezo@ibm.com","Ernest","Fernandez","8607928732","BSA"),
	("Ralph","West",'M',10,"603 Esker Junction","Oakland","Ca","94611","5109248062","rpattersonp@t.co","Ralph","Patterson","2023536461","BSA"),
	("Clarence","Castillo",'M',11,"21350 Calypso Lane","Tulsa","Ok","74149","9185432653","jfloresq@soundcloud.com","Jeffrey","Flores","8175264055","BSA"),
	("Joyce","Shaw",'F',10,"45 Marquette Place","Norfolk","Va","23551","7575853148","triverar@163.com","Tina","Rivera","4784326569","GSA"),
	("Michael","Mitchell",'M',11,"435 Sycamore Trail","San Diego","Ca","92127","7607570980","jadamss@reference.com","Jose","Adams","2029067625","BSA"),
	("Adam","Washington",'M',12,"45 Kinsman Center","Mobile","Al","36610","2517077494","acampbellt@google.com.au","Anthony","Campbell","2512795035","BSA");
CREATE TABLE SED_Database.sedUI_course(
	class_id ,
	class_name VARCHAR(50),
	class_description VARCHAR(500)
);
INSERT INTO sedUI_course
	(class_name, class_description)
VALUES
	("Astronomy","In learning about astronomy, Scouts study how activities in space affect our own planet and bear witness to the wonders of the night sky: the nebulae, or giant clouds of gas and dust where new stars are born; old stars dying and exploding; meteor showers and shooting stars; the moon, planets, and a dazzling array of stars."),
    ("Aviation","For most of history, people have dreamed of flying, imagining how it would feel to soar through the sky like an eagle or hover in midair like a hummingbird, to float on unseen currents, free of Earth's constant tug, able to travel great distances and to rise above any obstacle. Today, through aviation, we can not only join the birds but also fly farther, faster, and higher than they ever could."),
    ("Chemistry","Chemistry explores how substances react with each other, how they change, how certain forces connect molecules, and how molecules are made are all parts of chemistry. Stretch your imagination to envision molecules that cannot be seen—but can be proven to exist—and you become a chemist."),
    ("Composite Materials","	Composites can be found just about everywhere: in airplanes and sports cars, golf clubs and guitars, boats and baseball bats, bathtubs and circuit boards, and even bridges. Composites make bicycles and skis lighter, kayaks and canoes stronger, houses warmer, and helmets tougher."),
    ("Drafting","	Drafting is a highly refined form of drawing used to communicate ideas to engineers, architects, and craftspeople. In earning this badge, Scouts learn the importance of accuracy and simplicity in developing a drawing that shows precise details in a simple format."),
    ("Electricity","Electricity is a powerful and fascinating force of nature. As early as 600 BC, observers of the physical world suspected that electricity existed but did not have a name for it. In fact, real progress in unraveling the mystery of electricity has come only within the last 250 years."),
    ("Electronics","Electronics is the science that controls the behavior of electrons so that some type of useful function is performed. Today, electronics is a fast-changing and exciting field.	"),
    ("Energy","Saving, producing, and using energy wisely will be critical to America's future. If we are to leave future generations with a world in which they can live as well or better than we have, Scouts and other potential leaders of tomorrow must begin the hard work of understanding energy and the vital role it will play in the future."),
    ("Engineering","Engineers use both science and technology to turn ideas into reality, devising all sorts of things, ranging from a tiny, low-cost battery for your cell phone to a gigantic dam across the mighty Yangtze River in China."),
    ("Game Design","Scouts begin by learning gaming terminology and analyzing various types of games they’ve played. They then pick one game, tweak its rules or objectives, and track how the changes affect players’ actions and emotional experiences. After that, they design a new game, a process that includes writing rules, creating a prototype, and play-testing. "),
    ("Model Design","Model making, the art of creating copies of objects that are either smaller or larger than the objects they represent, is not only an enjoyable and educational hobby: it is widely used in the professional world for such things as creating special effects for movies, developing plans for buildings, and designing automobiles and airplanes."),
    ("Nuclear Science","Nuclear science gives us a simple explanation of the natural world. The ultimate goal of nuclear science is to find out if there is one fundamental rule that explains how matter and forces interact. Earning the Nuclear Science merit badge is a chance for Scouts to learn about this exciting field at the cutting edge of science today."),
    ("Oceanography","The oceans cover more than 70 percent of our planet and are the dominant feature of Earth. Wherever you live, the oceans influence the weather, the soil, the air, and the geography of your community. To study the oceans is to study Earth itself."),
    ("Programming","Earning the Programming merit badge will take you behind the screen for a look at the complex codes that make digital devices useful and fun. Without programs, today’s high-tech gadgets would be little more than empty shells. But given clear instructions, digital devices can do amazing things and perform operations that would have seemed like magic to people in the past."),
    ("Robotics","	Earning the Robotics merit badge requires a Scout to understand how robots move (actuators), sense the environment (sensors), and understand what to do (programming); he should demonstrate robot design in building a robot. You should help ensure that the Scout has sufficiently explored the field of robotics to understand what it is about, and to discover whether this may be a field of interest for him as a career."),
    ("Space Exploration","Space is mysterious. We explore space for many reasons, not least because we don't know what is out there, it is vast, and humans are full of curiosity. Each time we send explorers into space, we learn something we didn't know before. We discover a little more of what is there."),
    ("Sustainability","The sustainability badge aims to teach Scouts about climate change, species extinction, resource extraction, green chemistry, recycling, and zero-waste manufacturing."),
    ("Weather","Meteorology is the study of Earth's atmosphere and its weather and the ways in which temperature, wind, and moisture act together in the environment. In addition to learning how everyday weather is predicted, Scouts can learn about extreme weather such as thunderstorms, tornadoes, and hurricanes, and how to stay safe."),
    ("Radio","Radio is a way to send information, or communications, from one place to another. Broadcasting includes both one-way radio (a person hears the information but can't reply) as well as two-way radio (where the same person can both receive and send messages)."),
    ("Computers","Technology has come a long way since Computers merit badge was first introduced in 1967. This badge will teach Scouts about technology in the digital age."),
    ("Inventing","Inventing involves finding technological solutions to real-world problems. Inventors understand the importance of inventing to society because they creatively think of ways to improve the lives of others. Explore the world of inventing through this new merit badge, and discover your inner inventiveness.");
CREATE TABLE SED_Database.sedUI_location(
	location_id ,
	class_name VARCHAR(50),
	class_description VARCHAR(500)
);
INSERT INTO sedUI_location
	(street,city,state,zip_code,building,room_number,capacity)
VALUES
	("1959 Sage Trail","Ocala","FL",34474,"Aivee",96,53),
	("42869 Holmberg Point","Bismarck","ND",58505,"Aivee",32,72),
	("5 Merry Plaza","El Paso","TX",79950,"Skidoo",27,94),
	("3 Hazelcrest Place","Tacoma","WA",98424,"Youspan",18,53),
	("7 Village Trail","Bakersfield","CA",93386,"Riffpedia",70,68),
	("5 Manitowish Street","North Little Rock","AR",72199,"Wordware",18,81),
	("96516 Southridge Circle","Oklahoma City","OK",73124,"Feedmix",45,98),
	("396 Veith Avenue","Jamaica","NY",11447,"Trunyx",97,100),
	("32629 Anniversary Parkway","Atlanta","GA",30368,"Browseblab",75,64),
	("25093 Chinook Pass","Little Rock","AR",72222,"Gigabox",77,65),
	("41131 Everett Way","El Paso","TX",88546,"Riffpedia",82,98);
INSERT INTO sedUI_staff
	(first_name,last_name,staff_type,phone_number,email,street,city,state,zip_code,activity_status)
VALUES
	("Donna","Burns",'I',"5514471666","dburns0@ifeng.com","29856 Talmadge Plaza","Young America","MN",55557,"A"),
	("Rachel","Bennett",'I',"9171051172","rbennett1@forbes.com","843 Reinke Court","Fresno","CA",93726,"A"),
	("Christina","Austin",'C',"6073904625","caustin2@blogtalkradio.com","97534 Independence Drive","Macon","GA",31296,"A"),
	("Jennifer","Parker",'C',"4947351760","jparker3@hc360.com","5482 Chinook Street","Stamford","CT",06922,"A"),
	("Thomas","Morales",'I',"6053293551","tmorales4@jalbum.net","9 Center Avenue","Tucson","AZ",85720,"A"),
	("Rose","Garza",'C',"2731291519","rgarza5@ox.ac.uk","261 Brown Avenue","Las Vegas","NV",89178,"A"),
	("Wanda","Hamilton",'I',"4801622865","whamilton6@hibu.com","0 Butterfield Pass","Harrisburg","PA",17110,"A"),
	("Clarence","Carroll",'C',"1815013018","ccarroll7@go.com","63 Summit Plaza","Albany","NY",12232,"A"),
	("Martin","Riley",'C',"5136044083","mriley8@google.co.uk","82 Florence Junction","San Rafael","CA",94913,"A"),
	("Christina","Clark",'I',"7452494625","cclark9@quantcast.com","92781 Debs Way","Huntsville","AL",35815,"A");
