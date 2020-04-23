Semaphore web app
=================

Running a local instance
------------------------

Install dependencies, create a sqlite DB and an admin user account on your local instance.

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

You may need to set an environment variable for DJANGO_SECRET_KEY.  Since it's just a local dev instance, any string value will do fine.

Running the tests
-----------------

`python manage.py test` will use the django test runner to run the tests.  If you'd rather have the tests run automatically on changes to files, you can use `ptw`.