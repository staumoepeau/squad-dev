# Project Name : MyWhy System

## How to Setup on Linux
1. Clone this project `git clone http://squad.eito.space/git/MyWhy/squad.git`
2. Go To Project Directory `cd squad`
3. Create a Virtual Environment `python3 -m vevn env`
4. Activate Virtual Environment `source env/bin/activate`
5. Install Requirements Packages `python3 -m pip install -r requirements.txt`
6. Install Mysql Client `python3 -m pip install mysqlclient`
7. Login to your Mysql Server and Create Database `CREATE DATABASE squad`
8. Change the Database Settings on the settings.py
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'squad', 
			'PASSWORD': 'your root password',
			'USER' : 'root',
			'HOST' : 'localhost'
		}
9. Do the Migrations `python3 manage.py makemigrations`
10. Migrate the Database `python3 manage.py migrate`
11. Create Super User `python3 manage.py createsuperuser`
12. Run the Server `python3 manage.py runserver`
13. Login