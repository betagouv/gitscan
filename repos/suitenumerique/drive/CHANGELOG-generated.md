## Changelog : drive (30 derniers jours, au 23/10/2026)

### Résumé
Ce mois-ci, LaSuite Drive a franchi une étape importante en optimisant ses performances pour les grands volumes de données et en enrichissant ses outils d'administration. Les capacités de surveillance (monitoring) et de sécurité ont également été considérablement renforcées pour garantir une plateforme plus robuste, pilotable et sécurisée pour les administrateurs et les utilisateurs.

### Évolutions fonctionnelles
- **Améliorations de l'administration** :
    - Nouveaux outils de gestion des utilisateurs : fusion de comptes, transfert de fichiers entre utilisateurs et filtrage par adresse email.
    - Visibilité accrue sur le stockage : affichage des quotas de stockage, identification des fichiers les plus volumineux et gestion des limites par utilisateur directement dans l'interface d'administration.
    - Suivi de l'activité : affichage de la date de dernière connexion des utilisateurs.
- **Gestion des fichiers et quotas** :
    - Possibilité d'exclure certains éléments (et leurs descendants) du calcul du quota de stockage.
    - Amélioration de la fiabilité des uploads grâce à une réservation systématique de l'espace disque avant le transfert.
- **Contrôle du SDK** : Ajout d'une option de configuration permettant d'activer ou de désactiver l'affichage des pages liées au SDK.

### Évolutions techniques
- **Performances** :
    - Optimisations massives des requêtes SQL pour l'affichage des listes d'éléments, des favoris, des récents et de la corbeille, permettant une navigation fluide même sur des bases de données volumineuses.
    - Optimisation du calcul des accès hérités et des liens d'ancêtres dans les listes d'éléments.
- **Observabilité et Analytics** :
    - Mise en place de métriques Prometheus complètes (performances de la base de données, files Celery et métriques métier).
    - Intégration du suivi d'événements via Posthog (création par template, export de dossiers, suppression d'éléments, édition de documents, etc.).
- **Sécurité** :
    - Renforcement de la vérification des preuves de requêtes WOPI.
    - Mise en place de limitations de débit (*rate limiting*) sur les points de terminaison de création d'éléments.
    - Application de plusieurs correctifs de sécurité critiques sur les dépendances backend et frontend.
- **Infrastructure et DevOps** :
    - Migration du stockage objet local vers RustFS (remplaçant MinIO).
    - Optimisation des processus de build Docker pour le frontend.
    - Amélioration des déploiements Helm (ajout de moniteurs de métriques et gestion de l'ingress).
    - Automatisation des tâches de gestion via Celery Beat.

### Autres changements
- **Documentation** : Documentation des métriques Prometheus et mise à jour des exemples de serveurs de ressources.
- **Nettoyage** : Suppression de composants d'authentification inutilisés et nettoyage de valeurs codées en dur.
