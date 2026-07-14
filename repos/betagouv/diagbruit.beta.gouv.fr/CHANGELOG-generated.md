## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles fonctionnalités liées aux alertes de bruit, notamment l'intégration de données de zones à bruit et de certificats acoustiques. Des optimisations de performance significatives ont été apportées aux pipelines de données et à l'ingestion de données, ainsi que des corrections de bugs et des améliorations de la sécurité.

### Évolutions fonctionnelles
- Ajout d'une première version des alertes de zones à bruit, incluant l'affichage de badges et l'intégration de données Strapi.
- Implémentation d'un système de certificats acoustiques, avec la possibilité d'ajouter des recommandations.
- Amélioration du zoom sur les préconisations (PRECO).
- Ajout d'un lien vers la documentation dans le pied de page.
- Possibilité de relier une parcelle via l'URL.
- Ajout d'un champ "référence" pour les données.
- Intégration des données routières INFRA, avec correction d'une duplication.
- Ajout de la possibilité de filtrer les données par code département.

### Évolutions techniques
- Optimisation des performances des pipelines de données, notamment en parallélisant les requêtes et en optimisant les requêtes SQL.
- Amélioration de l'ingestion des données, avec une gestion plus efficace de la mémoire et une correction des problèmes de duplication.
- Refonte de l'architecture d'ingestion des données pour supporter les données GeoJSON.
- Mise en place d'un système d'authentification plus robuste.
- Migration de l'exécution de dbt vers Dagster pour une meilleure gestion et visibilité des pipelines.
- Utilisation de `uv` pour construire les images Docker, améliorant ainsi les performances.
- Amélioration de la gestion des variables d'environnement pour dbt sur Scalingo.
- Correction de problèmes liés à la gestion des dépendances et des versions de dbt.
- Mise à jour des fixtures de tests pour refléter les changements dans les données.

### Autres changements
- Correction de plusieurs bugs mineurs liés à l'affichage et à la gestion des données.
- Nettoyage du code et suppression de commentaires inutiles.
- Amélioration de la documentation.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Amélioration de la sécurité en corrigeant des vulnérabilités potentielles.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Correction de problèmes liés à l'indexation par les moteurs de recherche.
- Amélioration de l'accessibilité du site web.
- Correction de problèmes de liens brisés.
- Mise à jour des métadonnées pour améliorer le référencement.
