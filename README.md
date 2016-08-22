#SED Web Registration Application Development

This program is in development and is to be used for the Mitre Scout Engineering Day as a Registration Web Service. This program is for the front end of the registration service and is written in HTML, JavaScript, PHP and CSS. Anyone who would like to make please contact Ryan Dufrene at rdufrene@mitre.org.

## Installation

These instructions use [Git Bash](https://git-for-windows.github.io/):

1. [Install Git Bash.](https://git-scm.com/downloads)
2. [Install XAMPP.](https://www.apachefriends.org/index.html)
3. Open Git Bash.
4. Clone the source code into C:\xampp\htdocs: 
```
git clone https://github.com/crabbymonkey/sed.git /c/xampp/htdocs/ScoutEngineeringDay
```

## Usage

1. Open XAMPP Control Panel.
2. Start Apache Service by clicking the start button.
3. If not running a MySQL Database start the MySQL service using the start button. 
4. Open your browser of choice.
5. Go to the URL [http://localhost/ScoutEngineeringDay/navbar/index.html](http://localhost/ScoutEngineeringDay/navbar/index.html) (This may change)

## Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## To Do

- [ ] Finish Navbar
- [ ] Create Home page
- [ ] Create Login page
- [ ] Create Register page
- [ ] Create Course List page
- [ ] Create Scout List page
- [ ] Create Single Scout page
- [ ] Create Single Course page
- [x] Create PHP connection to the database
- [ ] Create getScoutInfoFromDatabase()
- [ ] Create getAllScoutsFromDatabase()
- [ ] Create getCourseInfoFromDatabase()
- [ ] Create getAllCoursesFromDatabase()

## Credits

* **Ryan Dufrene**: Developer - *Initial work*
* **Edward Gedeon**: Developer - *Initial work*
