# Django Blog usage 
install postgres
brew install postgresql

start postgres
pg_ctl -D ~/Documents/databases/postgres -l logfile start

stop postgres
pg_ctl stop

restart service : 
brew services restart postgresql

create user : 
/opt/homebrew/bin/createuser -s postgres

create database : 
/opt/homebrew/bin/createdb -U postgres blogdatabase

connect to database : 
psql -d postgres

set password : 
\password 

connect to database : 
psql -d postgres -U postgres


run django migrations : 
python manage.py makemigrations                                   
python manage.py migrate
python manage.py showmigrations


run django app : 
python manage.py runserver 

python manage.py createsuperuser
email : a@a.com
username : a
password : a
