cd example_com
rm example.sqlite3
python manage.py syncdb --noinput
sqlite3 example.sqlite3 < admin.sql
python manage.py runserver &
sleep 1
echo "$!" > django.pid
curl -I http://localhost:8000/polls/ && echo "server started."
