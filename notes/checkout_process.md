1. Back up fixtures
   python manage.py dumpdata myrest --format json --indent 4> myrest/fixtures/users.json

   python manage.py loaddata myrest/fixtures/users.json
