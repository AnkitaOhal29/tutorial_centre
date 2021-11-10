# TutorialCentre
Backend python code

## Clone the project
Clone the tutorial_centre project from GitHub:

```bash
Project Root Directory: `/var/www`
git clone remote url
```
##  Change into project directory

```bash
cd <project_name>
```

##  Install Python

```bash
sudo apt-get update && sudo apt-get install python3.7 virtualenv
```

##  OS Dependencies

```bash
sudo apt-get update &&  sudo apt-get install python3-dev python3.7-dev build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev
```

##  Database
Create empty database for the application (e.g. demo_login ) :

##  Create virtual env :

```bash
virtualenv -p python3.7 env_name
```

##  Activate the environment:

```bash
source env_name/bin/activate
```

##  Install Dependencies

```bash
pip install -r requirements.txt
```

##  Migrate Database

```bash
python manage.py makemigrations
python manage.py migrate
```
## Create super user

```bash
python manage.py createsuperuser
```

##  Finally, run the development server:

```bash
python manage.py runserver
```
    
The project will be available at 127.0.0.1:8000.