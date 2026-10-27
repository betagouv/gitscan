## Changelog : data-inclusion (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilisation des flux de données et le renforcement de la sécurité de l'API. Les utilisateurs bénéficient d'une recherche sémantique enrichie et du rétablissement de l'exportation des statistiques. En parallèle, l'infrastructure a été simplifiée et les processus d'ingestion ont été optimisés pour gagner en robustesse.

### Évolutions fonctionnelles
- **Recherche sémantique** : Intégration et affichage des services à distance dans les résultats de recherche.
- **Statistiques** : Rétablissement de la fonctionnalité d'exportation des données statistiques.

### Évolutions techniques
- **Sécurité et API** :
    - Renforcement de la protection des données : les jetons (tokens) de widget sont désormais exclus des liens de feedback et des journaux d'erreurs (Sentry).
    - Amélioration de la validation côté serveur pour les téléchargements (contrôle des tailles et des formats).
    - Sécurisation de la gestion des jetons et de la validation des hôtes autorisés pour les widgets.
- **Pipelines de données** :
    - Simplification du pipeline par la suppression de l'ingestion "monenfant" et de ses composants associés.
    - Optimisation de l'ingestion DORA pour s'adapter aux nouvelles structures de données.
    - Amélioration de la robustesse des processus via la validation des archives avant extraction et le nettoyage des champs de données inutilisés.
- **Infrastructure et Déploiement** :
    - Refonte des politiques d'accès aux données (buckets) pour une meilleure segmentation des droits de lecture et d'écriture.
    - Mise à jour et optimisation des composants d'infrastructure (Traefik, MLflow, et renommage de composants de pilotage).
    - Stabilisation de l'environnement via le gel de certaines dépendances critiques.
