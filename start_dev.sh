# reload of this script should be handled via entr
python manage.py collectstatic --noinput && python manage.py runserver --noreload