# FILEMAN
Lightweight Web File manager

# Authors and acknowledgment
- Themba Maphosa
- Siviwe Qolohle
- Momelezi Mchunu

# Running and intalling the application

There is quite a number of libraries needed to run the application, and to ensure it runs as it should they should be installed.
1. Set up a virtual environment.
2. Use the following command to install the needed modules: *pip install -r requirements.txt*
3. Run *npm install* to ensure you have the tailwindcss module.
4. Ensure that you have Postgresql set up for the database to work
5. Make sure you have a .env file that points to the database information
6. You shoud be good to go after these steps

## Setting up POSTGRESQL
1. Download postgresql : *sudo apt install postgresql postgresql-contrib*
2. Start the postgresservice : *sudo systemctl start postgresql.service*
3. Log into postgres terminal and create a database: *CREATE DATABASE dbname;*
4. Create user for the project and grnat necessary permissions: *CREATE USER user WITH PASSWORD 'password'; GRANT ALL PRIVILEGES ON DATABASE dbname TO user;*
5. From here onwards you can run the *init.py* to create the tables
