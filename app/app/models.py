from peewee import SqliteDatabase, Model, CharField, DateTimeField, IntegerField

db = SqliteDatabase('models.db')

class ZennArticlesModel(Model):
    url = CharField()
    article_type = CharField()
    title = CharField()
    likes = IntegerField()
    date = DateTimeField()

    class Meta:
        database = db


db.create_tables([
    ZennArticlesModel
])
