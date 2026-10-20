## Changelog : drive (30 derniers jours, au 19 octobre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance significative de l'outil d'administration et une optimisation majeure des performances pour les bases de données volumineuses. Les administrateurs disposent désormais de leviers beaucoup plus précis pour gérer les utilisateurs et les quotas de stockage. Parallèlement, le système est devenu plus robuste et observable grâce à l'intégration de nouveaux outils de monitoring et de suivi d'activité.

### Évolutions fonctionnelles

**Administration (Interface d'administration)**
- **Gestion des utilisateurs** : Possibilité de fusionner des comptes, de transférer des éléments d'un utilisateur à un autre et de filtrer les utilisateurs partageant une même adresse e-mail.
- **Gestion des quotas** : Amélioration du contrôle du stockage avec l'affichage des quotas complets, des fichiers les plus volumineux et la possibilité d'exclure certains éléments (et leurs descendants) du calcul du quota.
- **Visibilité accrue** : Affichage de la dernière date de connexion des utilisateurs et de la version actuelle du logiciel dans l'en-tête.
- **Gestion des doublons** : Possibilité de désactiver les doublons les moins récemment utilisés.

**Utilisateurs et API**
- **Corbeille** : Amélioration de la visibilité de la corbeille pour ne lister que les éléments appartenant aux sous-arborescences possédées par l'utilisateur.
- **Téléchargement** : Amélioration du processus d'upload avec une réservation de la taille du fichier déclarée avant l'autorisation du transfert.
- **Interface** : Masquage automatique des pages liées au SDK lorsque celui-ci est désactivé.

### Évolutions techniques

**Performances et Optimisation**
- **Requêtes de données** : Optimisation massive des performances pour la récupération des listes d'éléments, des favoris et des éléments récents (utilisation de plages de chemins et de sous-requêtes pour éviter les scans de tables complets).
- **Arborescence** : Accélération de la recherche des ancêtres et des liens de parenté pour les éléments de la corbeille et des listes.

**Observabilité et Monitoring**
- **Métriques Prometheus** : Mise en place de métriques détaillées (base de données, files d'attente Celery, métriques métier) via un endpoint `/metrics`.
- **Suivi d'activité (Posthog)** : Intégration de l'événementiel pour suivre les actions clés (création via modèle, conversion, export de dossier, suppression, édition de documents).

**Infrastructure et Sécurité**
- **Déploiement (Helm/Docker)** : Ajout de moniteurs de métriques et d'ingress dans Helm ; optimisation de la construction des assets frontend dans Docker.
- **Stockage** : Remplacement de MinIO par RustFS pour le stockage objet en environnement local.
- **Sécurité** : Mise en place de la limitation du débit (rate limiting) sur la création d'éléments et renforcement de la vérification des preuves de requêtes WOPI.
- **Fiabilité** : Amélioration de la gestion des connexions à la base de données (pool psycopg) et de la planification des tâches asynchrones avec Celery Beat.

### Autres changements
- **Documentation** : Documentation des métriques Prometheus et mise à jour des exemples de serveurs de ressources.
- **Outils de développement** : Ajout de commandes pour profiler les points de terminaison de l'API et générer des jeux de données de taille de production.
