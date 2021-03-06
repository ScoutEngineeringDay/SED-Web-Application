# SED Web Registration Application Development

This program is in development and is to be used for the Mitre Scout Engineering Day as a Registration Web Service. The front end of the registration service and is written in HTML, JavaScript, Python and CSS; with the database using MySQL. Anyone who would like to help with development please contact Ryan Dufrene at rdufrene@mitre.org, or Walter Hiranpat at whiranpat@mitre.org.

Please review the License, Code of Conduct and Contributing documentation.

# Installation

The installation of this web application is done using the [ScoutEngineeringDay/SED-Deployments](https://github.com/ScoutEngineeringDay/SED-Deployments) repository, please review the instillation instructions found there.


## Recompiling Website Code
After making changes to the code located in `/your_location_choice/SED-Deployments/content/SED-Web-Application` you will notice that the website will not automatically update.

The following steps will update the local delpyment of the website:
1. Open command line of your choosing.
2. Enter the folder that holds the repository: `cd /your_location_choice/SED-Deployments`
3. SSH into the Vagrant mechine: `vagrant ssh`
4. Enter the code source: `/ansible`
5. Run the update script: `./SED-web-update.sh`

Wait for the site to recompile and then refresh [http://localhost:8080/](http://localhost:8000/).


## URLs:

* Local host urls:
  - [http://localhost:8080/](http://localhost:8000/): Local Website Home Page
  - [http://localhost:8080/admin/](http://localhost:8000/admin/): Local	Admin Page

* Main Test Website url:
  - [http://www.sedteam.com/](http://www.sedteam.com/): Website Home Page
  - [http://www.sedteam.com/admin/](http://www.sedteam.com:/admin/): Website Admin Page


## Contributing
Before contributing please make sure you meet the requirements stated in the CONTRIBUTING.md file

### Process to contribute as non-member of the team:
1. Fork the project
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Design

![SED_Software.png](SED_Software.png?raw=true "Scout Engineering Day Web Design")

## Database Design Schema:

![SED_DataBase.jpg](SED_DataBase.jpg?raw=true "Scout Engineering Day Database")

## Credits
Developer Team(2016):
* **Sue Kim**: Manager - *Initial work*
* **Ryan Dufrene**: Front-End Developer - *Initial work*
* **Walter Hiranpat**: AWS, Django Back-End Developer, Database Developer - *Initial work*
* **Edward Gedeon**: Front-End Developer -  *Initial work*

Developer Team(2017):
* **Sue Kim**
* **Ryan Dufrene**
* **Walter Hiranpat**
* **Phillip Marlow**
* **Kaylee White**
* **Joseph Mahakian**
* **Joel Stien**

Developer Team(2018):
* **Sue Kim**: Managment
* **Ryan Dufrene**: Front End
* **Walter Hiranpat**: Back End
* **Phillip Marlow**: Deployment
* **Kaylee White**: Design
* **Kevin Codera**: Test
