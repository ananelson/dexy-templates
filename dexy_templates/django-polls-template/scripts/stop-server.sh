DJANGO_PID=`cat mysite_com/django.pid`
pkill -TERM -P $DJANGO_PID
curl -I http://localhost:8000/polls/ || echo "server stopped."
