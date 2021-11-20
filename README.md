
## local env
```bash
$ export PYTHONDONTWRITEBYTECODE=1 #no cache
$ export DB_SECRET='{"password":"password","dbname": "dev","port": 5432,"username": "dev_api","host": "localhost"}'
$ uvicorn main:app --reload --port 5000 
```

## tips
clean docker `docker-compose down --rmi all --volumes --remove-orphans`