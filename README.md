# My_Site

<p align="center">
  <img src="https://user-images.githubusercontent.com/29748439/130503888-ee2103cc-267f-4cfc-9ae7-b9da19f41a86.png">
  <h1 align="center">
    Django Tutorial Project
  </h1>
  <h3 align="center"> This is a full blog website backend written with django </h3>
  <h4 align="center"> This backend model is written by fbv( Functional Based View) method </h4>
<h6 align="center">The full project for Django fundemental course in maktabkhooneh.org.</h6>
</p>

### Overview
- [Overview](#overview)
- [Built With](#Built-With)
- [Download & Setup Instructions](#Download_&_Setup_Instructions)
- [Running the Project](#Running_the_Project)
- [Database schema](#database-schema)
- [Bugs or Opinion](#bugs-or-opinion)

### Built With
<p> This section is the list of languages used in this project.</p>

---

<p align="center" >
<img src="https://github.com/wsvincent/awesome-django/raw/main/assets/django-logo-positive.svg" alt="database schema"  margin="20px" width="70" height="70"/>
<img src="https://hugovk.github.io/python-logos/img/EuroPython%20Society.png" alt="database schema" margin="20px"  width="70" height="70"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg"  margin="20px" alt="bootstrap" width="70" height="70"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"  margin="20px" alt="html5" width="70" height="70"/>
<img src="http://3con14.biz/code/_data/js/intro/js-logo.png" alt="js"  margin="20px" width="70" height="70"/>
<img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite"  margin="20px" width="70" height="70"/>
</p>

---

## Download & Setup Instructions :

After downloading the project, make sure to create a virtual enviroment and  install [project's requirements.](https://github.com/Novin1380/mysite-main/blob/main/requirements.txt)

Clone the project. This will download the GitHub respository files onto your local machine.

```Shell
git clone https://github.com/Novin1380/mysite-main.git
```
installing virtual enviroment and activating:
```Shell
pip install virtualenv
```
Windows setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
venv\Scripts\activate

#deactivating enviroment
deactivate
```
Linux and Mac setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
source venv/bin/activate

#deactivating enviroment
deactivate
```

then installing the requirements:

```Shell
pip install -r requirements.txt
```
### Running the Project
in order to run the project you need to use either ways below

default and development settings
```Shell
python manage.py runserver 
#or
python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.dev
```
production settings
```Shell
python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.prod
```
<strong>Note:</strong> if you want to change the settings permanently to prod you can modify the settings in enviroment varibale inside the manage.py and need to use dokcer or install the mysql directly on your machine

### Database schema :
this is the model schema have been used in this project:
![drawSQL-export-2021-08-23_23_26](https://user-images.githubusercontent.com/29748439/130503854-cefc63a6-1466-4164-825a-9f313d521059.png)

### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.

---

<h6 align="center">be kind with each other and share your problems solution to makes better world!</h6>
<h5 align="center">just enjoy! 👋</h5>

