## Changelog : messages (30 derniers jours)

### Résumé
Les dernières mises à jour de Messages apportent des améliorations significatives à la sécurité, aux performances et aux fonctionnalités. Les utilisateurs bénéficieront d'une meilleure expérience avec l'ajout de nouvelles options d'import/export de boîtes aux lettres, d'améliorations de l'éditeur de messages et de corrections de bugs pour une utilisation plus fluide. Des optimisations techniques ont également été réalisées pour améliorer la stabilité et l'évolutivité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un bouton d'aide configurable dans l'en-tête (#537).
- Possibilité d'exporter une boîte aux lettres au format mbox, avec les libellés (#553).
- Ajout du support de l'importation de fichiers PST et du streaming de données pour les fichiers mbox (#544).
- Ajout d'une liste noire pour les préfixes de boîtes aux lettres personnelles (#540).
- Ajout d'une disposition multi-colonnes pour l'éditeur de signatures (#551).
- Ajout d'un bouton d'impression dans le menu contextuel des messages (#518).
- Possibilité d'ajouter des images directement dans le corps des messages via l'éditeur BlockNote (#539, #527).
- Ajout d'une option d'autofocus dans les compositeurs de messages, de modèles et de signatures.
- Amélioration de la gestion des libellés et dépliement automatique des parents actifs (#547).
- Amélioration de la formulation dans la boîte de sortie (#539).

### Évolutions techniques
- Migration vers la nouvelle API Drive sans recherche d'espace de travail (#558).
- Ajout du support de la plateforme ARM64 pour les constructions d'images Docker (#554).
- Mise à jour des étapes des workflows GitHub Actions (#555).
- Amélioration des vérifications DNS avec des enregistrements configurables (#522).
- Ajout d'événements de tâches Celery pour la surveillance des workers (#549).
- Refonte de l'expérience développeur avec uv, rustfs, caddy et un nouveau Makefile (#556).
- Mise à jour de Django-lasuite de 0.0.19 à 0.0.24 (#546).
- Optimisation de la sérialisation et de la gestion du corps des MessageTemplate (#545).
- Ajout d'un throttling des destinataires des messages sortants (#506).
- Utilisation d'un webhook et d'une journalisation au lieu d'un pushgateway pour les auto-vérifications (#550).
- Ajout d'une commande de gestion pour afficher tous les utilisateurs de l'instance.
- Amélioration de la gestion des promesses asynchrones pour l'enregistrement et l'envoi des messages.

### Autres changements
- Ajout d'un lien de navigation ignoré pour les utilisateurs de clavier (#573).
- Ajout d'un backend DeployCenter pour la synchronisation des administrateurs de maildomain (#572).
- Correction d'un problème de position du curseur lors du clic dans les champs de saisie de la combobox (#534).
- Correction d'un bug empêchant la fermeture du panneau gauche lors du clic sur un dossier actif sur mobile.
- Suppression des fichiers de traduction Django et des catalogues de traduction backend.
- Mise à jour de Keycloak vers la version 26.5.4 (#571, #543).
- Mise à jour des dépendances frontend.
- Correction de problèmes liés à la construction des artefacts frontend pour les architectures amd64 et arm64.
- Correction de problèmes liés au cache npm.
- Publication de la version 0.3.0.
- Publication de la version 0.2.0.
- Suppression des caractères NUL du contenu des e-mails (#524).
- Ajout de protections contre les failles XSS (#520).
- Prévention d'IDOR sur les champs thread et mailbox de ThreadAccess (#557).
