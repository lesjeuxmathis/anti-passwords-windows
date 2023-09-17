#by lesjeuxmathis
import tkinter as tk
import os
import subprocess
import ctypes
from tkinter import simpledialog, messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def remove_password():
    username = simpledialog.askstring("Supprimer le mot de passe", "Entrez le nom de l'utilisateur :")
    if username:
        try:
            subprocess.call(['net', 'user', username, ''], shell=True)
            messagebox.showinfo("Succès", f"Le mot de passe de l'utilisateur {username} a été supprimé avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer le mot de passe : {str(e)}")

if is_admin():
    root = tk.Tk()
    root.title("Supprimer le mot de passe d'un utilisateur")

    remove_button = tk.Button(root, text="Supprimer le mot de passe", command=remove_password)
    remove_button.pack(padx=20, pady=20)

    root.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
