# SED Web Registration Application Development with Django Framework

This program is in development and is to be used for the Mitre Scout Engineering Day as a Registration Web Service. This program is for the front end of the registration service and is written in HTML, JavaScript, PHP and CSS. Anyone who would like to help with development please contact Ryan Dufrene at rdufrene@mitre.org.

## Installation

These instructions use [Git Bash](https://git-for-windows.github.io/):


## Usage

<<<<<<< HEAD
1. Open XAMPP Control Panel.
2. Start Apache Service by clicking the start button.
3. Start MySQL Database to start the MySQL service 
      1. Open a browser of choice.
      2. Go to the URL: [http://localhost/phpmyadmin/import.php](http://localhost/phpmyadmin/import.php)
      3. Under the "Import" tab and run schema.sql to generate the overall database schema
      4. Run the following .sql scripts in order for testing purposes:
          1. scout_script, class_script, location_script, staff_script, question_list
          2. workshop_script, security_Question_script, health_script
4. Open your browser of choice.
5. Go to the URL [http://localhost/ScoutEngineeringDay/index.html](http://localhost/ScoutEngineeringDay/index.html) (This may change)
=======
>>>>>>> 6152db7543fb8620cc7b9267a962f33aabfd9dd0

## Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

<<<<<<< HEAD
=======
## Django Commands

python manage.py makemigration
	when database have been altered
python manage.py migrate
	when database alter has occured and need update
python manage.py runserver
	to run the machine on localhost port 8000
python manage.py createsuperuser
	this will create you an admin level account 

## URLs:

http://localhost:8000/
	This will take you to website page
http://localhost:8000/admin/
	Allow you to log in to website admin site to modify database and create user and assigned them permissions

>>>>>>> 6152db7543fb8620cc7b9267a962f33aabfd9dd0
## Design

![ScoutEngineeringDayWebDesign.png](ScoutEngineeringDayWebDesign.png?raw=true "Scout Engineering Day Web Design")

<<<<<<< HEAD
Database Schema:
=======
## Database Design Schema:

>>>>>>> 6152db7543fb8620cc7b9267a962f33aabfd9dd0
![Relationship_Schema.png](Relationship_Schema.png?raw=true "Scout Engineering Day Database")
## To Do

Gui:

- [x] Finish Navbar
- [x] Create Home page
- [x] Create Login page
- [x] Create Register page
- [ ] Create Course List page
- [ ] Create Scout List page
- [ ] Create Single Scout page
- [ ] Create Single Course page
- [x] Create PHP connection to the database
- [x] Create getScoutInfoFromDatabase()
- [x] Create getAllScoutsFromDatabase()
- [x] Create getCourseInfoFromDatabase()
- [x] Create getAllCoursesFromDatabase()

## Credits

* **Ryan Dufrene**: Front-End Developer - *Initial work*
* **Edward Gedeon**: Front-End Developer - *Initial work*
* **Walter Hiranpat**: Database Developer - *Initial work*
<<<<<<< HEAD
* **Sue Kim**: Manager - *Initial work*
=======
* **Sue Kim**: Manager - *Initial work*
>>>>>>> 6152db7543fb8620cc7b9267a962f33aabfd9dd0
