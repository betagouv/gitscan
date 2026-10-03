## Changelog : meet (30 derniers jours, au 2 octobre 2026)

### Résumé
Ce mois-ci, meet a considérablement enrichi l'expérience de partage d'écran avec l'ajout de contrôles de zoom et de panoramique. L'accessibilité a été renforcée et la flexibilité accrue en permettant aux visiteurs non connectés de démarrer des réunions. Parallèlement, un effort majeur a été déployé pour renforcer la sécurité du système et stabiliser l'infrastructure de développement.

### Évolutions fonctionnelles
- **Partage d'écran** : Ajout de fonctionnalités de zoom et de panoramique, incluant des contrôles via la souris, la molette et des raccourcis clavier.
- **Accessibilité** : Amélioration de la navigation au clavier pour les outils de partage et ajout d'indices visuels pour les raccourcis de zoom.
- **Expérience utilisateur** : 
    - Possibilité pour les visiteurs non authentifiés de lancer une réunion.
    - Tri des participants en salle d'attente par ordre d'arrivée.
    - Amélioration des notifications sonores et visuelles lors de l'arrivée de participants.
    - Clarification des messages concernant l'état de l'enregistrement vidéo.
- **Enregistrement** : Meilleure gestion des échecs d'enregistrement (LiveKit egress) et ajout de la possibilité de configurer l'encodage via l'API.

### Évolutions techniques
- **Sécurité** : 
    - Correction massive de vulnérabilités critiques (CVE) sur plusieurs composants clés (Django, PyJWT, libssl, libexpat, etc.).
    - Mise en place de limitations (throttling) sur la génération de liens de réunion et de quotas quotidiens pour la création de salles.
    - Anonymisation des données sensibles (redaction) envoyées vers Sentry.
- **Infrastructure & Stockage** : 
    - Migration vers Garage pour le stockage S3 en environnement de développement et pour les services média.
    - Automatisation de la purge des salles inactives via un job planifié (cronjob).
- **Environnement de développement (DevEx)** : 
    - Modernisation de la stack de développement (passage à Node 22, version unique de Redis).
    - Amélioration du support pour Podman (mode rootless).
    - Mise à jour des pipelines CI/CD avec l'intégration de scans de vulnérabilités (Menshen) et la migration vers des workflows partagés.
- **Observabilité & Performance** : 
    - Optimisation de la gestion des logs (réduction du bruit et suivi de la durée des requêtes).
    - Amélioration des performances via le refactoring des caches de présence et de la gestion du lobby.

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant la purge des salles inactives et réorganisation du changelog.
- **Nettoyage** : Suppression de workflows Crowdin, de templates GitHub et de composants API inutilisés.
