# Neighborhood

## Author  
[Amimo] is the author of this project. Contact information of the author [gilbertmatete6@gmail.com]
  
# Description  
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.
  
##  Live Link  
 Click [View Site](https://nostalgia001.herokuapp.com/)  to visit the site

  
## Screenshots 
###### Home page
 
![](https://photos.google.com/photo/AF1QipNMriuKLSAs4nyjD2ZIqyv90k2XCeqJDeTEQxV9)
 
 ###### Gallery

![](https://photos.google.com/photo/AF1QipO1728Mj5k5xxqR1anI2MhjtI41bX2D_dRBGYTT)
 
## Using the Application
  
* create an account or sign up
* Go to your profile and select edit profile from the dropdown
* Choose your neighbourhood then save
* Proceed to submit your neighbourhood post. 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/AmimoG/Neighborhood 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
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
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6] 
* [Django 3.2] 
* [Heroku]
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  

## Contributing
Pull requests are welcome. For any changes that one intends to make, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Released under MIT License

Copyright (c) 2020 Amimo Matete.

[MIT](https://choosealicense.com/licenses/mit/)
