## Changelog : tchap-x-android (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations majeures concernant la gestion des médias, la recherche et la sécurité. Les utilisateurs peuvent désormais envoyer plusieurs fichiers ou images à la fois, utiliser une recherche globale plus performante et profiter d'une expérience plus fluide lors de la connexion. Des correctifs importants ont également été apportés pour stabiliser l'application et améliorer la clarté de l'interface, notamment en mode sombre.

### Évolutions fonctionnelles
- **Gestion des médias** : 
    - Support de l'envoi multiple de fichiers et d'images.
    - Amélioration de l'affichage des images en cours d'envoi et de la gestion des légendes.
    - Correction de la transparence lors du partage de fichiers avec des types MIME imprécis.
- **Communication et Recherche** :
    - Introduction d'une recherche globale permettant de chercher à la fois dans les salons et dans les messages ([#7410](https://github.com/tchapgouv/tchap-x-android/pull/7410)).
    - Amélioration des sondages avec la possibilité de sélectionner plusieurs réponses.
    - Optimisation de la suggestion de mentions dans les discussions.
- **Expérience Utilisateur (UX)** :
    - Correction de l'affichage des couleurs de la snackbar en mode sombre.
    - Amélioration de la fluidité de l'écran de sélection du fournisseur de compte (rendu scrollable).
    - Meilleure gestion des notifications, notamment pour garantir leur caractère "bruyant" même lorsque le contenu est masqué par un code PIN.
    - Correction de divers problèmes d'affichage (tailles de texte, champs de saisie sous le clavier).
- **Onboarding et Comptes** :
    - Possibilité de se connecter via l'adresse email partagée par Tchap Classique.
    - Amélioration du processus de création de compte et de la gestion des identifiants.

### Évolutions techniques
- **Noyau et Performance** :
    - Intégration et optimisation du SDK Rust, incluant des corrections pour les architectures arm64.
    - Activation du scan de contenu et intégration du scan antivirus.
    - Optimisation des processus de synchronisation et de la gestion de la base de données lors des mises à jour.
- **Architecture et Code** :
    - Refactorisation massive pour améliorer la maintenabilité : renommage des classes d'événements (singularisation), réorganisation des packages (session, DI) et nettoyage des imports.
    - Ajout d'une documentation technique exhaustive (KDoc) sur l'ensemble des interfaces de l'API.
    - Amélioration de la gestion des erreurs (dialogues d'erreur lors de l'échec d'envoi de message [#7470](https://github.com/tchapgouv/tchap-x-android/pull/7470)).
- **DevOps et CI/CD** :
    - Automatisation des processus de release via Fastlane et de nouveaux scripts de déploiement.
    - Activation des statistiques analytiques PostHog.

### Autres changements
- **Documentation** : Ajout de guides d'utilisation (notamment pour la sauvegarde automatique de Tchap Classique) et mise à jour de la documentation technique.
- **Maintenance** : Nettoyage régulier du linter et mise à jour des captures d'écran pour les boutiques d'applications.
