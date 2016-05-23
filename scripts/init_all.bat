call activate.bat
rem xpython
python manage.py syncdb --noinput
python manage.py migrate
python manage.py create_default_super_user
