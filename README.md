# efiling-gujhc

This is an application for Document Viewing and Verification for e-filing at Gujarat High Court.

## Environment Setup
This project has been made in Anaconda environment for package management. To install the required libraries, run the following command:

```bash
conda create --name myenvname --file package-list.txt
```

Here 'myenvname' will be the name of your environment for deployment of this project.

## Project Setup

Once the environment is prepared, we can start to use this repo to clone the project.

But first, we need to do initlization of our project before cloning (for security reasons, some files are not uploaded here).

```bash
django-admin start project efiling .
```

This will initialize the project files.

After this, simply replace the files from repo either by cloning the master or downloading the relavent master zip.

To clone the repo, you can use following command and enter relevant credentials:
```bash
git clone https://github.com/sarvang00/efiling-gujhc.git
```

## Database Setup
This project has been made in PostgresQL.

A database shall be required to be made in POSTGRES (version 10 and above supported) with the name of 'efiling'.

Then migrations will be required to be made.

Follow this command to create a note for changes and migrations.

```bash
python manage.py makemigrations
```

Resolve error messages, if any. Else continue to make migration to database:
```bash
python manage.py migrate
```

If you see no error messages, congratulations! Your project database has been successfully setup.

## Superuser and Groups setup

Once the database is setup, the first recommended step is to make a superuser.

That can be done by using the following command in the project terminal:
```bash
python manage.py createsuperuser
```
From here, you can follow the superuser instructions.

Now your app is ready in most spaces (and with some tweaks in your settings.py, for deployment!)


## Initial Setup

To use the application, the following command needs to be run:
```bash
python manage.py runserver
```

Once superuser is setup, he/she is supposed to login by visiting the admin dashboard and fulfilling the rest of the Admin form.

After that, they need to create 3 groups, namely:
    1. "Judges"
    2. "Advocates"
    3. "Officers"

After that, they can log out.

### Notice
This is a private project which may or may not be passed on to the High Court of Gujarat. Any unauthorized access and sharing of any of the code here may be liable to be prosecuted by law. 

--
Sarvang Dave,
23 May, 2020, 
Ahmedabad, Gujarat, India
