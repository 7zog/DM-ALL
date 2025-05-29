
---

# 📨 DM All

Un Bot Discord simple pour envoyer un message privé à tous les membres Non-Bots d’un serveur.

---

## 🚀 Fonctionnalités

* Envoie un message personnalisé à tous les membres non-bots d’un serveur
* Affiche la progression dans la console
* Gère les erreurs sans interrompre l’envoi
* Limite automatique la vitesse pour éviter les blocages (rate limits)
* Usage réservé aux administrateurs du serveur

---

## ⚙️ Prérequis

* Python 3.8 ou supérieur
* Un bot Discord avec un token valide
* Permissions Discord activées sur le bot :

  * `MESSAGE_CONTENT`
  * `MEMBERS`
  * `SEND_MESSAGES`
  * `DIRECT_MESSAGES`

---

## 🧱 Installation

1. Clone le dépôt :

   ```bash
   git clone https://github.com/7zog/DM-ALL.git
   cd DM-ALL
   ```

2. Installe les dépendances :

   * Sous **Windows**, double-clique sur `requirements.bat` pour installer automatiquement les packages.
   * Sinon, lance dans un terminal :

     ```bash
     pip install -r requirements.txt
     ```

---

## 🔧 Utilisation

1. Lance le bot :
   * Sous **Windows**, double-clique sur `star.bat` pour lancer automatiquement le script.
   * Sinon, lance dans un terminal :
   ```bash
   python dmall.py
   ```

2. Entre le token du bot quand demandé.

3. Dans un canal du serveur, envoie :

   ```
   &dm Ton message ici
   ```

---

## 🔐 Sécurité

* Seuls les administrateurs peuvent utiliser la commande.
* Les bots sont ignorés.
* Le bot envoie les messages avec une pause pour éviter les blocages liés au rate limit.

---

⚠️ Utilise ce bot de façon responsable. L’envoi massif de DM peut être sanctionné par Discord.

---
