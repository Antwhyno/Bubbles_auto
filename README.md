**Bubbles**

Fichier qui lance automatiquement la page de veille de windows

Il se lance toutes les 5 min si le pc n'est pas utilisé (détecte l'utilisation du clavier et de la souris)

** Installation fichier **

Lancement silencieux en arrière-plan
Pour que le script tourne en tâche de fond invisible dès le démarrage du PC :

Renommez votre fichier en .pyw (par exemple idle_bubbles.pyw). L'extension .pyw masque la fenêtre de terminal noire.

Placez un raccourci de ce fichier dans le dossier de démarrage Windows :

appuyez sur **Win + R**, entrez **shell:startup** et collez-y le raccourci.

**Plus de détails**

# 🫧 Windows Idle Bubbles Launcher

Script Python léger et autonome permettant de surveiller l'inactivité du clavier et de la souris sous Windows afin de déclencher automatiquement l'animation d'économiseur d'écran native **Bubbles.scr** (Bulles).

---

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Code source (`bubbles_idle.pyw`)](#-code-source-bubbles_idlepyw)
- [Guide d'installation et d'organisation](#-guide-dinstallation-et-dorganisation)
  - [1. Créer un dossier permanent](#1-créer-un-dossier-permanent)
  - [2. Enregistrer le fichier en `.pyw`](#2-enregistrer-le-fichier-en-pyw)
  - [3. Configurer le démarrage automatique](#3-configurer-le-démarrage-automatique)
- [Configuration et personnalisation](#-configuration-et-personnalisation)
- [Gestion et arrêt du script](#-gestion-et-arrêt-du-script)
- [Dépannage](#-dépannage)

---

## ✨ Fonctionnalités

- **Détection matérielle native** : Utilise l'API Win32 (`GetLastInputInfo`) pour suivre avec précision les entrées utilisateur sans consommation excessive de ressources.
- **Exécution silencieuse** : Fonctionne totalement en tâche de fond grâce à l'interpréteur `pythonw.exe` (aucune fenêtre noire / terminal).
- **Non-bloquant** : Ne lance qu'une seule instance de l'animation à la fois.

---

## ⚙️ Prérequis

- **Système d'exploitation** : Windows 10 ou Windows 11
- **Python** : Python 3.8+ installé (avec l'option *Add Python to PATH* activée)
- **Fichier système** : `C:\Windows\System32\Bubbles.scr` (présent par défaut sous Windows)

---