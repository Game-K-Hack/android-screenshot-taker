# Screenshot Taker
Application Python permettant des prendre automatiquement des imprim-écran d'una application. Actullement il est calibré pour l'application **RealPrice** (
[`com.app.realprice`](https://play.google.com/store/apps/details?id=com.app.realprice)), mais si vous voulez l'adapter pour votre application, il vous suffit de modifier le fichier `main.py`.

### Utilisation
Il faut que vous aillez le logiciel **Android Studio**, et installé au moins un **AVD** (Android Virtual Device). De plus, assurez vous d'avoir bien installé toutes les librairie Python.
Puis lancer simplement l'application `main.py`.

### Modification
Si vous voulez adapater cette application pour votre application, vous pouvez créer vos propre command en utilisant l'outil **adb** en modifiant `service/taker.py`. Voici les fonctionnalité que j'utilise pour mon application:

| Fonction | Description |
| -------- | ----------- |
| `change_lang_and_restart` | Change la langue de l'application, puis la redémmarre |
| `tap_id` | Simule un click sur l'élément suivant l'id de l'élément récupérable dans les layout de l'application. Exemple `android:id="@+id/currency_input_money_amount"`, l'id est donc `currency_input_money_amount` |
| `clear_text` | Supprime un champ text en appuyant `n` fois sur la touche `backspace`. |
| `add_text` | Ajouter un text au champ text |
| `take_screenshot` | Prendre un imprim-écran de l'émulateur Android |
