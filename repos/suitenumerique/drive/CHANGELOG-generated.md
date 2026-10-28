## Changelog : drive (30 derniers jours, au 27/10/2026)

### Résumé
Ce mois a été marqué par une montée en puissance significative de la plateforme, notamment grâce à une optimisation massive des performances pour supporter de grands volumes de données. L'expérience d'administration a été considérablement enrichie avec de nouveaux outils de gestion des utilisateurs et des quotas, tandis que la gestion des permissions de dossiers et la sécurité (notamment via le protocole WOPI) ont été renforcées pour garantir une navigation plus fluide et sécurisée.

### Évolutions fonctionnelles
- **Gestion des accès et dossiers :**
  - Amélioration de l'expérience sur les dossiers restreints : aperçu possible sans chargement de contenu, correction du fil d'Ariane et gestion plus intuitive des confirmations de suppression.
  - Amélioration de la fluidité du partage de dossiers lors de changements de restrictions d'accès.
- **Administration renforcée :**
  - Nouveaux outils de gestion des utilisateurs : possibilité de fusionner des comptes, de transférer des éléments d'un utilisateur à un autre et de filtrer les utilisateurs par email.
  - Meilleure visibilité administrative : affichage des dernières connexions, de la version actuelle et des quotas de stockage par utilisateur.
  - Gestion fine des quotas : possibilité de définir des exclusions de quota pour des éléments spécifiques et de leurs descendants.
- **Expérience utilisateur :**
  - Optimisation du processus d'upload avec réservation de la taille déclarée et limitation de débit (rate limiting) pour protéger le système.
  - Amélioration de la gestion de la corbeille pour les utilisateurs.

### Évolutions techniques
- **Performances et scalabilité :**
  - Optimisation majeure des requêtes de navigation et de recherche : utilisation d'index de chemin (path index) et de sous-requêtes pour éviter les scans de tables complets, permettant une réactivité accrue sur de très gros jeux de données.
  - Optimisation de la récupération des métadonnées et des ancêtres des éléments.
- **Observabilité et monitoring :**
  - Intégration de métriques Prometheus pour le suivi de l'infrastructure (base de données, files Celery) et des indicateurs métier.
  - Mise en place d'un suivi analytique via Posthog pour les actions clés (création via template, export de dossier, suppression, édition de documents).
- **Sécurité :**
  - Application de correctifs de sécurité critiques sur plusieurs dépendances (Django, PyJWT, Pillow, Certifi, etc.).
  - Renforcement de la sécurité WOPI : vérification accrue des preuves de requêtes et isolation des téléchargements de fichiers (sandboxing).
- **Infrastructure et CI/CD :**
  - Amélioration des pipelines de tests E2E avec l'utilisation d'images Playwright officielles.
  - Optimisation des builds Docker pour le frontend et ajustements des sondes de disponibilité (readiness probes) dans Helm.
  - Automatisation de l'exécution des commandes de gestion via Celery Beat.

### Autres changements
- **Documentation :** Mise à jour de la documentation concernant les métriques Prometheus et les scénarios de test de taille de fichiers.
- **Maintenance :** Nettoyage de code (suppression d'options Pylint obsolètes et de backends d'authentification inutilisés) et gestion des versions (releases v0.24.0 à v0.25.3).
