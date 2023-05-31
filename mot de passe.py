import random
import string
import csv
import tkinter
from tkinter import messagebox


def generate_password(length, include_special_chars):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_and_save():
    web = web_entry.get()
    user = user_entry.get()
    length = int(length_entry.get())
    include_special_chars = special_chars_var.get()

    password = generate_password(length, include_special_chars)
    password_output.delete("1.0", tkinter.END)
    password_output.insert(tkinter.END, password)

    # Enregistrement du mot de passe dans un fichier CSV
    filename = 'mot_de_passe.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([web, user, password])
    messagebox.showinfo("Enregistrement terminé", f"Le mot de passe a été enregistré dans {filename}")

# Création de la fenêtre principale
window = tkinter.Tk()
window.title("Générateur de mot de passe")

web_label= tkinter.Label(window, text="Entrer le nom du site")
web_label.pack()
web_entry = tkinter.Entry(window)
web_entry.pack()

user_label= tkinter.Label(window, text="Entrer le nom d'utilisateur")
user_label.pack()
user_entry=tkinter.Entry(window)
user_entry.pack()
# Étiquettes et champs de saisie pour les informations
length_label = tkinter.Label(window, text="Taille du mot de passe :")
length_label.pack()
length_entry = tkinter.Entry(window)
length_entry.pack()

special_chars_var = tkinter.BooleanVar()
special_chars_checkbutton = tkinter.Checkbutton(window, text="Inclure des caractères spéciaux", variable=special_chars_var)
special_chars_checkbutton.pack()

generate_button = tkinter.Button(window, text="Générer et Enregistrer", command=generate_password_and_save)
generate_button.pack()

# Sortie du mot de passe généré
password_output = tkinter.Text(window, height=1, width=30)
password_output.pack()

# Lancement de la boucle principale de l'interface
window.mainloop()