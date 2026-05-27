from tkinter import END, ACTIVE
from CRUD_lib.model import User, users


listbox_lista_obiektow = None
entry_imie = None
entry_nazwisko = None
entry_liczba_postow = None
entry_lokalizacja = None
button_dodaj_uzytkownika = None

label_imie_szczegoly_obiektu_wartosc = None
label_nazwisko_szczegoly_obiektu_wartosc = None
label_liczba_postow_szczegoly_obiektu_wartosc = None
label_lokalizacja_szczegoly_obiektu_wartosc = None

map_widget = None


def init_controller(
        listbox,
        entry_name,
        entry_surname,
        entry_posts,
        entry_location,
        button_add,
        label_name_value,
        label_surname_value,
        label_posts_value,
        label_location_value,
        map_view
):
    global listbox_lista_obiektow
    global entry_imie, entry_nazwisko, entry_liczba_postow, entry_lokalizacja
    global button_dodaj_uzytkownika
    global label_imie_szczegoly_obiektu_wartosc
    global label_nazwisko_szczegoly_obiektu_wartosc
    global label_liczba_postow_szczegoly_obiektu_wartosc
    global label_lokalizacja_szczegoly_obiektu_wartosc
    global map_widget

    listbox_lista_obiektow = listbox
    entry_imie = entry_name
    entry_nazwisko = entry_surname
    entry_liczba_postow = entry_posts
    entry_lokalizacja = entry_location
    button_dodaj_uzytkownika = button_add

    label_imie_szczegoly_obiektu_wartosc = label_name_value
    label_nazwisko_szczegoly_obiektu_wartosc = label_surname_value
    label_liczba_postow_szczegoly_obiektu_wartosc = label_posts_value
    label_lokalizacja_szczegoly_obiektu_wartosc = label_location_value

    map_widget = map_view


def add_marker(user):
    user.marker = map_widget.set_marker(
        user.coordinates[0],
        user.coordinates[1],
        text=user.imie
    )


def add_user_object(user):
    add_marker(user)
    users.append(user)


def show_users() -> None:
    listbox_lista_obiektow.delete(0, END)

    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, user.imie)


def clear_entries():
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_lokalizacja.delete(0, END)


def remove_user() -> None:
    i = listbox_lista_obiektow.index(ACTIVE)

    if users[i].marker:
        users[i].marker.delete()

    users.pop(i)
    show_users()


def show_user_details():
    i = listbox_lista_obiektow.index(ACTIVE)

    user = users[i]

    label_imie_szczegoly_obiektu_wartosc.config(text=user.imie)
    label_nazwisko_szczegoly_obiektu_wartosc.config(text=user.nazwisko)
    label_liczba_postow_szczegoly_obiektu_wartosc.config(text=user.posty)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=user.lokalizacja)

    map_widget.set_position(user.coordinates[0], user.coordinates[1])
    map_widget.set_zoom(12)


def edit_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    user = users[i]

    clear_entries()

    entry_imie.insert(0, user.imie)
    entry_nazwisko.insert(0, user.nazwisko)
    entry_liczba_postow.insert(0, user.posty)
    entry_lokalizacja.insert(0, user.lokalizacja)

    button_dodaj_uzytkownika.config(
        text="Zapisz zmiany",
        command=lambda: update_user(i)
    )


def update_user(i):
    users[i].imie = entry_imie.get()
    users[i].nazwisko = entry_nazwisko.get()
    users[i].posty = int(entry_liczba_postow.get())
    users[i].lokalizacja = entry_lokalizacja.get()

    users[i].coordinates = users[i].get_coordinates()

    if users[i].marker:
        users[i].marker.delete()

    add_marker(users[i])

    button_dodaj_uzytkownika.config(
        text="Dodaj użytkownika",
        command=add_user
    )

    clear_entries()
    entry_imie.focus()
    show_users()


def add_user():
    new_user = User(imie=entry_imie.get(),nazwisko=entry_nazwisko.get(),posty=int(entry_liczba_postow.get()),lokalizacja=entry_lokalizacja.get())

    add_user_object(new_user)

    clear_entries()
    entry_imie.focus()
    show_users()