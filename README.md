# hood


>[Stephen-Ndele](https://github.com/stephenndele)  
  
# Description  
Application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.
##  Live Link  
 Click [View Site](https://area-code.herokuapp.com/)  to visit the site
  
## Screenshots 
##### Home page
 
 ![Alt text](/media/hoodhome.png?raw=true "Main Page")

 ##### Single Hood page

 ![Alt text](/media/hood.png?raw=true "Main Page")

##### business Search

 ![Alt text](/media/business.png?raw=true "Main Page")

 
## User Story  
### as a User am able to:
* Register in the app be able to sign in  
* Set up a profile about me and a general location and my  neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department, fire department, and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
* View all available neighborhoods.
* Creates neighborhood

  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 git clone https://github.com/stephenndele/hood.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd hood 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations main
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 ### Api Endpoints
##### GET /api/v1/hoods

 * https://area-code.herokuapp.com/api/hood/

 ##### GET /api/v1/view_hood
 * https://area-code.herokuapp.com/api/view_hood/
 * 
 
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
    
## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2021 Stephen
 
## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
Reach me on:
>Email:  stephenndele093@gmail.com