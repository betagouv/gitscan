## Changelog : tchap-x-android (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'expérience utilisateur, notamment l'activation des commandes dans les messages, des badges plus clairs, et une meilleure gestion des salons privés. Des corrections de bugs et des mises à jour de sécurité ont également été intégrées.

### Évolutions fonctionnelles
- Ajout de la commande `/visio` pour lancer des appels vidéo. [#1234](https://github.com/tchapgouv/tchap-x-android/issues/1234)
- Activation des commandes dans les messages, permettant d'interagir directement depuis l'interface.
- Activation des salons privés non-chiffrés, offrant plus de flexibilité aux utilisateurs.
- Badge "Recommandé" ajouté pour les salons privés chiffrés, facilitant leur identification.
- Un texte d'alerte est maintenant affiché lors du partage d'un fichier dans un salon non chiffré.
- Suppression de l'affichage du bandeau de réinitialisation d'identité d'un membre.
- Le logo Tchap a été mis à jour dans le centre de notification (monochrome) et dans Android Studio.
- Renommage de l'application "Tchap beta" en "Tchap".
- Mise à jour des certificats de sécurité pour juillet 2026.

### Évolutions techniques
- Mise à jour de Compound à la version 10.2.1.
- Import de la version 26.06.2 d'Element X.
- Configuration des URL de Push en fonction de l'environnement.
- Suppression des noms de domaine Element non utilisés.
- Réduction de la taille des logs pour éviter les erreurs serveur.
- Changement du format de numéro de version.
- Correction de bugs liés à l'affichage du menu d'historique et à la construction de l'application.

### Autres changements
- Lien du Play Store ajouté au script de release.
- Suppression de la bordure pour les badges neutres.
- Mise à jour des captures d'écran.
