import ctypes
import os
import subprocess
import time

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

def get_idle_time_seconds():
    """Calcule les secondes écoulées depuis la dernière frappe ou mouvement de souris."""
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    # Différence entre le temps système global et le dernier événement
    elapsed_ms = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
    return elapsed_ms / 1000.0

IDLE_LIMIT = 1200  # Inactivité en secondes (ex: 20 minutes)
SCR_PATH = r"C:\Windows\System32\Bubbles.scr"

def main():
    if not os.path.exists(SCR_PATH):
        print(f"Erreur : Impossible de trouver {SCR_PATH}")
        return

    process = None

    while True:
        idle_seconds = get_idle_time_seconds()

        # Si le seuil d'inactivité est atteint et que l'animation n'est pas déjà lancée
        if idle_seconds >= IDLE_LIMIT:
            if process is None or process.poll() is not None:
                # Le paramètre /s lance l'écran de veille en plein écran
                process = subprocess.Popen([SCR_PATH, "/s"])
        
        time.sleep(2)

if __name__ == "__main__":
    main()