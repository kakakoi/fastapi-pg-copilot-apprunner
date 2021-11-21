from distutils.util import strtobool

import databases

import sqlalchemy

import os
import json
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

TEST_DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = TEST_DATABASE_URL
TESTING = os.environ.get('TESTING')
SECRET_NAME = 'FPCASVCCLUSTER_SECRET'
metadata = sqlalchemy.MetaData()
message = "go /docs"

try:
    TESTING = strtobool(TESTING)
    if TESTING == False:
        secret_text = json.loads(os.environ[SECRET_NAME])
        DATABASE = 'postgresql'
        USER = secret_text['username']
        PASSWORD = secret_text['password']
        # HOST = 'localhost'
        HOST = secret_text['host']
        PORT = secret_text['port']
        DB_NAME = secret_text['dbname']
        DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

except KeyError as e:
    print(f'EXCEPTION: {e}')
    message = 'Failed to Load: ENV (ToT)'
except sqlalchemy.exc.OperationalError as e:
    print(f'EXCEPTION: {e}')
    message = 'Failed to Load: STORAGE (ToT)'
except AttributeError as e:
    print(f'EXCEPTION: {e}')
    message = 'Failed to Load: ENV-NONE (ToT)'

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL
)