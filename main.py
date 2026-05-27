from tkinter import *
import tkintermapview

from CRUD_lib.model import User
from CRUD_lib.controler import (init_controller, show_users, remove_user, show_user_details, edit_user, add_user, add_user_object)


root = Tk()

root.title("Mapa znajomych")
root.geometry("1024x760")

# FRAME
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2, padx=50, pady=20)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# RAMKA LISTA OBIEKTOW
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista znajomych: ")
listbox_lista_obiektow = Listbox(ramka_lista_obiektow)

button_pokaz_szczegoly_obiektu = Button(ramka_lista_obiektow, text="Pokaz szczegoly", command=show_user_details)
button_usun_obiekt = Button(ramka_lista_obiektow, text="Usun", command=remove_user)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text="Edytuj", command=edit_user)

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

# RAMKA FORMULARZ

label_formularz = Label(ramka_formularz, text="Formularz: ")
label_imie = Label(ramka_formularz, text="Imię: ")
label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
label_liczba_postow = Label(ramka_formularz, text="Liczba postow: ")
label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")

label_formularz.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_liczba_postow.grid(row=3, column=0, sticky=W)
label_lokalizacja.grid(row=4, column=0, sticky=W)

entry_imie = Entry(ramka_formularz)
entry_nazwisko = Entry(ramka_formularz)
entry_liczba_postow = Entry(ramka_formularz)
entry_lokalizacja = Entry(ramka_formularz)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_liczba_postow.grid(row=3, column=1)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_uzytkownika = Button(ramka_formularz, text="Dodaj użytkownika", command=add_user)
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

# SZCZEGOLY OBIEKTU

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Szczegóły użytkownika")
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Imię: ")
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Nazwisko: ")
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
label_liczba_postow_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Liczba postów: ")
label_liczba_postow_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")
label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text="Lokalizacja: ")
label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text="...")

label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
label_imie_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1, sticky=W)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2, sticky=W)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3, sticky=W)
label_liczba_postow_szczegoly_obiektu.grid(row=1, column=4, sticky=W)
label_liczba_postow_szczegoly_obiektu_wartosc.grid(row=1, column=5, sticky=W)
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6, sticky=W)
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7, sticky=W)

# ramka mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=600, corner_radius=4)
map_widget.set_zoom(6)
map_widget.set_position(52.2, 21.0)

map_widget.grid(row=0, column=0)

init_controller(listbox=listbox_lista_obiektow, entry_name=entry_imie,
    entry_surname=entry_nazwisko, entry_posts=entry_liczba_postow, entry_location=entry_lokalizacja,
    button_add=button_dodaj_uzytkownika, label_name_value=label_imie_szczegoly_obiektu_wartosc,
    label_surname_value=label_nazwisko_szczegoly_obiektu_wartosc, label_posts_value=label_liczba_postow_szczegoly_obiektu_wartosc,
    label_location_value=label_lokalizacja_szczegoly_obiektu_wartosc, map_view=map_widget
)

add_user_object(User(imie="Jakub", nazwisko="Jakubowski", posty=2, lokalizacja="Warszawa"))
add_user_object(User(imie="Jan", nazwisko="Kowalski", posty=10, lokalizacja="Bydgoszcz"))
add_user_object(User(imie="Adam", nazwisko="Mickiewicz", posty=25, lokalizacja="Wilno"))

show_users()

root.mainloop()