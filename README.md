
## local
```bash
$ export PYTHONDONTWRITEBYTECODE=1 #no cache
$ export DB_SECRET='{"password":"password","dbname": "dev","port": 5432,"username": "dev_api","host": "localhost"}'
$ poetry install
$ poetry shell
$ cd backend
$ docker-compose up -d # app,db,pgadmin
```
```bash
$ uvicorn main:app --reload --port 5000 # app
```

## tips
clean docker `docker-compose down --rmi all --volumes --remove-orphans`