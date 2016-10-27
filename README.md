# SED Web Registration Application Development

This program is in development and is to be used for the Mitre Scout Engineering Day as a Registration Web Service. The front end of the registration service and is written in HTML, JavaScript, Python and CSS; while to back end is done using MySQL. Anyone who would like to help with development please contact Ryan Dufrene at rdufrene@mitre.org.


# Installation

The following tools are needed:
- [Git Bash](https://git-for-windows.github.io/)
- [Python](https://www.python.org/downloads/) (**Hint:** Make sure to check add to PATH if downloading version 3.5+)


## Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

<<<<<<< HEAD
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
=======

## First Time Setup

1. Open Git Bash
2. Install Django `pip install Django==1.10.2`
  * **Hint:** If it does not recognize pip you need to add the Python bin folder to Environment Variable PATH.
  * **Hint:** If you are within a company firewall you will have to use `pip install --proxy <proxy> Django==1.10.2`
3. Open location of source code `cd /locationofcode/sed`
4. Setup the Database `python manage.py makemigrations`
5. Apply Database `python manage.py migrate`
6. Run the server `python manage.py runserver`
  * Do not close the Git Bash window it is running the server.
7. Go to [http://localhost:8000/](http://localhost:8000/) in browser


## Useful Django Commands

- When database have been altered: `python manage.py makemigrations`
- When database alter has occured and need update: `python manage.py migrate`
- To run the machine on localhost port 8000: `python manage.py runserver`
- This will create you an admin level account: `python manage.py createsuperuser`


## URLs:

- [http://localhost:8000/](http://localhost:8000/): Website Home Page
- [http://localhost:8000/admin/](http://localhost:8000/admin/):	Admin Page

>>>>>>> 9ac481a003d3b9b5e650f8899651fb8571966e21

## Design

![ScoutEngineeringDayWebDesign.png](ScoutEngineeringDayWebDesign.png?raw=true "Scout Engineering Day Web Design")

<<<<<<< HEAD
=======

>>>>>>> 9ac481a003d3b9b5e650f8899651fb8571966e21
## Database Design Schema:

![Relationship_Schema.png](Relationship_Schema.png?raw=true "Scout Engineering Day Database")


## To Do

- [x] Finish Navbar
- [x] Create Home page
- [x] Create Login page
- [x] Create Register page
- [x] Create Course List page
- [x] Create Scout List page
- [x] Create Single Scout page
- [x] Create Single Course page
- [x] ~~Create PHP connection to the database~~
- [x] Create getScoutInfoFromDatabase()
- [x] Create getAllScoutsFromDatabase()
- [x] Create getCourseInfoFromDatabase()
- [x] Create getAllCoursesFromDatabase()
- [ ] Fix bugs created when switching to Django
- [ ] Add MySQL database
- [ ] Update Registration process

## Credits

* **Sue Kim**: Manager - *Initial work*
* **Ryan Dufrene**: Front-End Developer - *Initial work*
* **Walter Hiranpat**: Database Developer - *Initial work*
* **Edward Gedeon**: Front-End Developer - *Initial work*
