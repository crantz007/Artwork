from model import Artist
from model import Artwork

def display_menu_get_choice(menu):

    while True:
        choice = input('Enter choice? ')
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')

def message(msg):
    print(msg)

def show_artworks(artworks):

    if artworks:
        for artwork in artworks:
            print(artwork)
    else:
        print('No Artwork to display')

def get_artist_info():
    artist_name = input('Enter the artist name :')
    artist_email = input('Enter the artist email :')
    return Artist(artist_name=artist_name, artist_email=artist_email)

def get_artwork_info():
    artwork_name = input('Enter the artwork name : ')
    artwork_price = float(input('Enter the artwork price:'))
    return Artwork(artwork_name=artwork_name, artwork_price=artwork_price)

def get_artwork_id():
    while True:
        try:
            artwork_id = int(input('Enter Artwork ID: '))
            if artwork_id > 0:
                return artwork_id
            else:
                print('Enter a positive number: ')

        except ValueError:
            print('Enter a number :')

def get_sold_value():

     while True:
        reply = input('Enter \'sold\' if artwork is sold or \'available\' if artwork is available: ')
        if reply.lower() in ['sold', 'available']:
            return reply.lower() == 'sold'
        else:
            print('Type \'sold\' or \'available\'')





def ask_question(question):

    return input(question)


