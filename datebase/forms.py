from peewee import *


db = SqliteDatabase('my_hotels.db')


class BaseModel(Model):
    """У казываем какую базу данных будем использовать """

    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    user_name = CharField(max_length=40)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30, null=True)


class SearchHistory(BaseModel):
    user = ForeignKeyField(User, backref='search_history')
    search_query = CharField()
    timestamp = DateTimeField()
    image = BlobField()


db.create_tables([User, SearchHistory])
