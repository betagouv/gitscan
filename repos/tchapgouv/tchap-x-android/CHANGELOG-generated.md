## Changelog : tchap-x-android (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une meilleure gestion des salons privés, des corrections de bugs et des optimisations de l'interface. Des fonctionnalités de sécurité ont également été renforcées, avec l'ajout d'un écran d'expiration de compte et des améliorations concernant les certificats Let's Encrypt. Enfin, des mises à jour techniques ont été effectuées pour maintenir la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un badge "Recommandé" pour les salons privés chiffrés.
- Activation des salons privés non-chiffrés.
- Possibilité de partager un fichier dans un salon non chiffré avec un message d'alerte approprié.
- Suppression du support pour Android Auto (mode voiture).
- Renommage de la section "Direct" en "Personnes".
- Correction de l'icône d'envoi de message en mode sombre.
- Ajout d'un écran d'expiration de compte pour renforcer la sécurité.
- Amélioration de l'affichage des fichiers dans la vue média (taille, format).
- Possibilité de choisir des sons personnalisés pour les notifications de messages et d'appels.
- Amélioration de l'affichage des badges de mentions.
- Possibilité de basculer l'image dans l'éditeur d'image.
- Réorganisation des éléments dans les détails d'une salle.
- Ajout d'un indicateur du nombre de messages non lus dans la liste des salles.
- Amélioration de l'affichage des fichiers PDF et des fichiers texte dans la vue média.
- Possibilité de partager sa position avec des permissions plus granulaires.

### Évolutions techniques
- Mise à jour du SDK Matrix Rust en version 26.06.3.
- Mise à jour de Compound Design Tokens en version 10.2.1.
- Mise à jour de Maplibre GL Android SDK en version 13.2.0.
- Mise à jour de Roborazzi.
- Amélioration de la compilation du SDK Rust.
- Compilation du SDK en mode release par défaut.
- Optimisation de la taille des logs pour éviter les erreurs serveur.
- Correction de bugs liés à la compilation et au build.
- Correction de problèmes liés à l'intégration avec Element X v26.06.2.
- Correction de problèmes liés à l'utilisation de Vulkan (désactivation).
- Amélioration de la gestion des erreurs de localisation.
- Correction de problèmes liés aux tests unitaires et d'interface utilisateur.
- Correction de problèmes liés à l'utilisation de Let's Encrypt.
- Amélioration de la gestion des certificats.
- Correction de problèmes liés à la synchronisation des chaînes de caractères.
- Suppression de jobs cron et de clés SSH privées dans les forks.
- Correction de problèmes liés à la dérivation de clés SQLCipher.

### Autres changements
- Mise à jour des captures d'écran.
- Ajout de liens Figma pour certaines fonctionnalités.
- Corrections de linting et amélioration du script de release.
- Ajout d'options de débogage pour le build (mode dev, nombre de workers).
- Ajout d'une section "Rageshake & ClearCache" dans les paramètres avancés.
- Suppression de la version 0.11.0.
- Ajout d'une option pour signaler un problème avec un numéro de ticket GitHub.
- Suppression de la possibilité de définir un style de carte personnalisé.
- Amélioration de la gestion des erreurs et des logs.
- Corrections diverses et amélioration de la qualité du code.
