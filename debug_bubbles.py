import ctypes
import os
import subprocess
import time

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

# 1. Vérification de l'existence de Bubbles.scr
SCR_PATH = r"C:\Windows\System32\Bubbles.scr"
if not os.path.exists(SCR_PATH):
    # Contournement si Python 32-bit tourne sur un Windows 64-bit
    SCR_PATH = r"C:\Windows\Sysnative\Bubbles.scr"

print(f"[CHECK] Chemin de l'écran de veille : {SCR_PATH}")
print(f"[CHECK] Fichier trouvé : {os.path.exists(SCR_PATH)}")

if not os.path.exists(SCR_PATH):
    print("❌ ERREUR : Bubbles.scr est introuvable sur votre système.")
    input("Appuyez sur Entrée pour quitter...")
    exit()

def get_idle_seconds():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    # GetTickCount64 évite les bugs si le PC est allumé depuis longtemps
    current_tick = ctypes.windll.kernel32.GetTickCount64() & 0xFFFFFFFF
    return (current_tick - lii.dwTime) / 1000.0

print("\n--- Test d'inactivité (Seuil réglé à 5 secondes pour tester) ---")
print("Ne touchez plus à la souris ni au clavier...\n")

IDLE_LIMIT = 5  # Réduit à 5s pour le test

while True:
    idle = get_idle_seconds()
    print(f"Inactivité détectée : {idle:.1f}s / {IDLE_LIMIT}s", end="\r")
    
    if idle >= IDLE_LIMIT:
        print(f"\n🚀 Seuil atteint ! Tentative de lancement de {SCR_PATH}...")
        try:
            # Lancement via shell pour gérer correctement l'extension .scr
            subprocess.Popen(f'"{SCR_PATH}" /s', shell=True)
            print("✅ Commande envoyée avec succès.")
            break
        except Exception as e:
            print(f"❌ Erreur lors de l'exécution : {e}")
            break
            
    time.sleep(1)

input("\nAppuyez sur Entrée pour terminer...")