### "check-version"
python -c "import django; print(django.get_version())"

### "create-project"
website="example_com"
django-admin.py startproject $website

### "tree"
tree --charset=ascii | strings

### "start"
#cd $project
#python manage.py runserver &
#sleep 3 # time to spool up
#curl -I http://localhost:8000
