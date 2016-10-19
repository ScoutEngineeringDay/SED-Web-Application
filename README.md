# SED Web Registration Application Development with Django Framework

This program is in development and is to be used for the Mitre Scout Engineering Day as a Registration Web Service. This program is for the front end of the registration service and is written in HTML, JavaScript, PHP and CSS. Anyone who would like to help with development please contact Ryan Dufrene at rdufrene@mitre.org.


# Installation

The following tools are needed:
- [Git Bash](https://git-for-windows.github.io/)
- [Python](https://www.python.org/downloads/)
- [SQLite](https://sqlite.org/)

## Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request


## First Time Setup

1. Open Git Bash
2. Install Django `pip install Django==1.10.2`
  * If it does not recognize pip you need to add the Python bin folder to Environment Variable PATH.
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


## Design

![ScoutEngineeringDayWebDesign.png](ScoutEngineeringDayWebDesign.png?raw=true "Scout Engineering Day Web Design")


## Database Design Schema:

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
* **Sue Kim**: Manager - *Initial work*
