import random
import string
import csv
import tkinter
import hashlib
import os
from tkinter import messagebox

os.chdir('C:\Test')

web_entry = "ABC"
user_entry = "ABC"
length_entry = 0
special_chars_var = False
password_output = "ABC"

# Création de la fenêtre génération de mot de passe
def window_generator_password():
    window = tkinter.Tk()
    window.title("password generator")

    web_label= tkinter.Label(window, text="Enter URL")
    web_label.pack()
    web_entry = tkinter.Entry(window)
    web_entry.pack()

    user_label= tkinter.Label(window, text="Enter user name ")
    user_label.pack()
    user_entry=tkinter.Entry(window)
    user_entry.pack()
    # Étiquettes et champs de saisie pour les informations
    length_label = tkinter.Label(window, text="Length password")
    length_label.pack()
    length_entry = tkinter.Entry(window)
    length_entry.pack()

    special_chars_var = tkinter.BooleanVar()
    special_chars_checkbutton = tkinter.Checkbutton(window, text="Include special chars", variable=special_chars_var)
    special_chars_checkbutton.pack()

    generate_button = tkinter.Button(window, text="Create and save", command=generate_password_and_save)
    generate_button.pack()

    # Sortie du mot de passe généré
    password_output = tkinter.Text(window, height=1, width=64)
    password_output.pack()

    # Lancement de la boucle principale de l'interface
    window.mainloop()
    return (web_entry, user_entry, length_entry, special_chars_var, password_output)

window_generator_password()

def generate_password(length, include_special_chars):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    salt = "mysecret"  # Sel secret pour renforcer le hachage
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

def generate_password_and_save():
    web = web_entry.get()
    user = user_entry.get()
    length = int(length_entry.get())
    include_special_chars = special_chars_var.get()

    password = generate_password(length, include_special_chars)
    hashed_password = hash_password(password)
    password_output.delete("1.0", tkinter.END)
    password_output.insert(tkinter.END, password)

    # Enregistrement du mot de passe dans un fichier CSV
    filename = "code.csv"
    if filename:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([web, user, hashed_password])
        messagebox.showinfo("It's save")
