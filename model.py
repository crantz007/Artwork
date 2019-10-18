from peewee import *
from database_config import database_path

db = SqliteDatabase(database_path)

class Artist(Model):

    artist_name = CharField()
    artist_email = CharField()


    class Meta:
        database = db
        primary_key = CompositeKey('artist_name','artist_email')
        constraints = [SQL('FOREIGN KEY(artwork_id','artwork_name)''REFERENCES artist(artist_name,artist_email)')]

    def __str__(self):
        sold_status = ' have been ' if self.sold else 'is available'
        return f'ID  artwork name :{self.artwork_name},artwork price: {self.artwork_price}.artwork{sold_status}'


db.connect()
db.create_tables([Artist])
db.close()


class Artwork(Model):
     artworkd_id = AutoField()
     artwork_name = CharField()
     artwork_price = FloatField()
     sold_artwork = BooleanField(default=False)

     class Meta:
         database = db



def __str__(self):
    sold_status = ' have been ' if self.sold else 'is available'
    return f'ID {self.id}, artwork name :{self.artwork_name},artwork price: {self.artwork_price}.artwork{sold_status}'


db.connect()
db.create_tables([Artwork])
db.close()