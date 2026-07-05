## Changelog : tchap-x-android (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'expérience utilisateur, notamment l'ajout de commandes dans les messages, l'amélioration de la gestion des salons privés et des badges, ainsi que des corrections de bugs et des optimisations de performance. Des modifications ont également été apportées à l'interface utilisateur et à la configuration de l'application.

### Évolutions fonctionnelles
- Ajout de la commande `/visio` pour lancer des appels vidéo.
- Activation des commandes dans les messages, permettant de nouvelles interactions.
- Activation des salons privés non-chiffrés.
- Badge "Recommandé" ajouté pour les salons privés chiffrés, facilitant leur identification.
- Renommage de la section "Direct" en "Personnes" pour une meilleure clarté.
- Suppression du support pour Android Auto (mode voiture).
- Amélioration des badges de mentions.
- Texte d'alerte amélioré lors du partage de fichiers dans un salon non chiffré.
- Masquage du bandeau de réinitialisation d'identité d'un membre.
- Remplacement du logo Tchap sur Android Studio.
- Rendu monochrome du logo Tchap dans le centre de notification.

### Évolutions techniques
- Mise à jour des certificats de juillet 2026.
- Mise à jour de Compound (version 10.2.1) et des thèmes (compound-design-tokens).
- Correction de la compilation du rust-sdk et compilation en mode release par défaut.
- Amélioration de la génération des snapshots des cartes et nettoyage automatique des anciennes.
- Réduction de la taille des logs pour éviter les erreurs serveur.
- Correction de bugs liés à l'affichage du menu d'historique et à la compilation.
- Vérification de la connexion avec le code de récupération si disponible.
- Limitation des espaces au mode consultation.

### Autres changements
- Changement du format de numéro de version.
- Renommage de l'application Tchap beta en Tchap.
- Suppression des noms de domaine Element non utilisés.
- Ajout de la commande `/visio`.
- Mise à jour des screenshots.
- Ajout des sections Rageshake & ClearCache dans les paramètres avancés.
- Correction de l'icône d'envoi de message en DarkMode.
