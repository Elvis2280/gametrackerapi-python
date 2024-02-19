from peewee import *
from utils.config import settings
from playhouse.db_url import connect

postgresqlConn = connect(settings.database_url)

try:
    postgresqlConn.connect()
    print("Database connection established")
except Exception as e:
    print(e)
    print("Database connection failed")


class BaseModel(Model):
    class Meta:
        database = postgresqlConn
