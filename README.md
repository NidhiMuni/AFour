# Setup instructions
* Install Python 3.8 from python.org
* Install Django: pip install Django
* Install Django REST Framework: pip install django djangorestframework django-cors-headers
* Install PostgreSQL from postgresql.org

# Setup test database
* Restore database using pg_restore: pg_restore -h localhost -p 5432 -U postgres -d qms -v "I:\Nidhi\AFour\dump-test_a4services-202007171941.backup"
* Setup a user with username = myprojectuser and password = password 

