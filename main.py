import peewee

import artworkstore
import ui
from Menu import Menu


def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break

def create_menu():
    menu = Menu()
    menu.add_option('1','Artist Name',artist_name)
    menu.add_option('2','Email',artist_email)
    menu.add_option('3', 'Artwork Name', artwork_name)
    menu.add_option('4', 'Price', artwork_price)
    menu.add_option('5', 'Show Sold Artwork ', show_sold_artwork)
    menu.add_option('6', 'Show All Artwork', show_all_artwork)
    menu.add_option('7', 'Show Available Artwork', show_available_artwork)
    menu.add_option('8', 'Add New Artwork', add_new_artwork)
    menu.add_option('9', 'Delete Artwork ',delete_artwork)
    menu.add_option('0', 'Change Artwork Status ', change_artwork_status)
    menu.add_option('S', 'Search Artwork ', search_artwork)
    menu.add_option('Q', 'Quit', quit_program)

    return menu

def artist_name():
    artist_name = ui.get_artist_info()
    try:
        artist_name.save()
    except peewee.IntegrityError:
        ui.message('Error, artist already exists in the database')

def artist_email():
    artist_email = ui.get_artist_info()
    try:
        artist_email.save()
    except peewee.IntegrityError:
        ui.message('Error, email already exists in the database')

def artwork_name():
    artwork_name = ui.get_artwork_info()
    try:
        artwork_name.save()
    except peewee.IntegrityError:
        ui.message('Error, artwork already exists in the database')

def artwork_price():
    artwork_price = ui.get_artwork_info()
    artwork_price.save()


def add_new_artwork():
    add_new_artwork = ui.get_artwork_info()
    try:
        add_new_artwork.save()
    except peewee.IntegrityError:
        ui.message('Error,- artwork already exists in the database')

def show_sold_artwork():
    sold_artwork = artworkstore.get_artwork_by_sold_value(True)
    ui.show_artworks(sold_artwork)

def show_available_artwork():
    available_artwork = artworkstore.get_artwork_by_available_value(False)
    ui.show_artworks(available_artwork)

def show_all_artwork():
    artworks = artworkstore.get_all_artwork()
    ui.show_artworks(artworks)

def delete_artwork():

    delete_artwork = ui.get_artwork_info()
    delete_artwork.delete()


def search_artwork():
    search_term = ui.ask_question('Enter search term, will match partial name or email')
    matches = artworkstore.search_artwork(search_term)
    ui.show_artworks(matches)


def change_artwork_status():
    artwork_id = ui.get_artwork_id()
    artwork = artworkstore.get_artwork_by_id(artwork_id)
    if not artwork:
        ui.message('artwork not found')
        return
    new_sold = ui.get_sold_value()
    artwork.sold = new_sold
    artwork.save()

def quit_program():
    ui.message('Thanks and Bye!')


if __name__ == '__main__':
    main()





