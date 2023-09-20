#by lesjeuxmathis
import tkinter as tk
import os
import subprocess
import ctypes
from tkinter import simpledialog, messagebox
import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        # Vous avez déjà des privilèges administratifs ici
        pass
    else:
        # Redémarre ce script avec des privilèges administratifs
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == '__main__':
    run_as_admin()
    
    # Votre code à exécuter avec des privilèges administratifs va ici
    # Par exemple, vous pouvez ajouter :
    # os.system("netsh interface set interface name='Local Area Connection' admin=enable")

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
