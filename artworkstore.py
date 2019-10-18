from model import Artwork
from model import Artist
from peewee import fn


def delete_artwork(artwork):
    rows_deleted = Artwork.delete().where(Artwork.id == artwork.id).execute()
    if not rows_deleted:
        raise ArtworkError('Artwork does not exists')


def get_artwork_by_id(artwork_id):
    return Artwork.get_or_none(Artwork.id == artwork_id)


def exact_match(artwork, artist,artwork_id):
    search = Artwork.get_or_none(
        (Artwork.id == artwork_id) & (Artwork.artwork_name == artwork.artwork_name) & (Artist.artist_name == artist.artist_name))
    return search is not None


def search_artwork(term):
    query = Artwork.select().where((fn.LOWER(Artwork.artwork_name).contains(term.lower())))
    return list(query)


def get_artwork_by_available_value(available):
    query = Artwork.select().where(Artwork.available == available)
    return list(query)


def get_artwork_by_sold_value(sold):
    query = Artwork.select().where(Artwork.sold == sold)
    return list(query)


def get_all_artwork():
    query = Artwork.select()
    return list(query)


def artwork_count():
    return Artwork.select().count()


class ArtworkError(Exception):
    pass


def artist_count():
    return Artist.select().count()


def search_artist(term):
    query = Artist.select().where((fn.LOWER(Artist.artist_name).contains(term.lower())))

    return list(query)


def get_artist_by_name(artist_name):
    return Artist.get_or_none(Artist.name == artist_name)


def delete_all_artwork():
    Artwork.delete().execute()


def delete_all_artist():
    Artist.delete().execute()
