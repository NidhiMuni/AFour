# Setup instructions
* Install Python 3.8 from python.org
* Install Django: pip install Django
* Install Django REST Framework: pip install django djangorestframework django-cors-headers
* Install PostgreSQL from postgresql.org

# Setup test database
* Create a new empty database called qms 
* Restore database using pg_restore: pg_restore -h localhost -p 5432 -U postgres -d qms -v "<repository root>\Data\dump-test_a4services-202007171941.backup"
* Setup a new user "myprojectuser" and grant privileges to access tables in QMS database: psql -h localhost -d qms -U postgres -p 5432 -a -q -f "<repository root>\Data\QmsDbConfiguration.sql"

# Execution instructions
* Open a command prompt and change directory to the folder where the repository is cloned
* Run the following command to start the web server: python manage.py runserver
* Once it is running, you can call the APIs

# APIs
* /api/employees
** This returns a JSON of all employees in the database
** It takes an optional query parameter coe_id to return employees in the given coe_id. For example, /api/employees?coe_id=AFTC0629 will return the list of employees in the given COE


