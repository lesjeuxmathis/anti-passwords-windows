#by lesjeuxmathis
import os
import sys
import ctypes
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
from tkinter import ttk

# Dictionnaire de traduction pour les chaînes
translations = {
    'en': {
        'title': "Remove User Password",
        'prompt': "Enter the username:",
        'success': "The password for user {} has been successfully removed.",
        'error': "Unable to remove the password: {}",
        'button_text': "Remove Password",
    },
    'fr': {
        'title': "Supprimer le mot de passe d'un utilisateur",
        'prompt': "Entrez le nom de l'utilisateur :",
        'success': "Le mot de passe de l'utilisateur {} a été supprimé avec succès.",
        'error': "Impossible de supprimer le mot de passe : {}",
        'button_text': "Supprimer le mot de passe",
    },
}

# Fonction pour définir la langue actuelle
def set_language(lang):
    global current_language
    current_language = lang
    update_ui()

# Fonction pour mettre à jour l'interface utilisateur avec la langue actuelle
def update_ui():
    if current_language in translations:
        translation = translations[current_language]
        root.title(translation['title'])
        remove_button.config(text=translation['button_text'])

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        # Vous avez déjà des privilèges administratifs ici
        return
    else:
        # Redémarre ce script avec des privilèges administratifs s'il n'est pas déjà en cours d'exécution en tant qu'administrateur
        if getattr(sys, 'frozen', False):
            # Exécution en tant qu'exécutable autonome
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            # Exécution en tant que script Python
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join([sys.argv[0]] + sys.argv[1:]), None, 1)
        sys.exit()

def remove_password():
    username = simpledialog.askstring(translations[current_language]['title'], translations[current_language]['prompt'])
    if username:
        try:
            subprocess.call(['net', 'user', username, ''], shell=True)
            messagebox.showinfo(translations[current_language]['title'], translations[current_language]['success'].format(username))
        except Exception as e:
            messagebox.showerror(translations[current_language]['title'], translations[current_language]['error'].format(str(e)))

# Définir la langue par défaut (anglais)
current_language = 'en'

if __name__ == '__main__':
    run_as_admin()

    # Créer la fenêtre principale
    root = tk.Tk()

    # Titre de la fenêtre en fonction de la langue actuelle
    root.title(translations[current_language]['title'])

    # Menu déroulant pour choisir la langue
    lang_label = ttk.Label(root, text="Language:")
    lang_label.pack()
    lang_combo = ttk.Combobox(root, values=list(translations.keys()))
    lang_combo.set(current_language)
    lang_combo.pack()
    lang_combo.bind("<<ComboboxSelected>>", lambda event: set_language(lang_combo.get()))

    # Bouton pour supprimer le mot de passe
    remove_button = tk.Button(root, text=translations[current_language]['button_text'], command=remove_password)
    remove_button.pack(padx=20, pady=20)

    # Mettre à jour l'interface utilisateur avec la langue actuelle
    update_ui()

    root.mainloop()
