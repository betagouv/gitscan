## Changelog : zero-logement-vacant (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la sécurité et de l'authentification, avec une migration vers Better Auth. Des corrections de bugs et des améliorations de la performance ont également été apportées, notamment au niveau de l'export de données et de la gestion des perimètres. Enfin, de nouvelles fonctionnalités ont été implémentées, comme la possibilité de créer des campagnes à partir de groupes et d'ajouter des documents aux campagnes.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des campagnes à partir de groupes de logements.
- Possibilité d'ajouter des documents aux campagnes, avec une nouvelle interface et des endpoints dédiés.
- Amélioration de la visualisation des perimètres sur la carte, avec la possibilité de les afficher ou de les masquer.
- Correction d'un bug empêchant l'affichage correct des étiquettes énergétiques dans les exports de données.
- Correction d'un problème de filtrage intercommunal dans la recherche de logements.
- Ajout d'une option pour ne pas contacter les propriétaires dans la gestion des logements.
- Amélioration de la gestion des utilisateurs Cerema LOVAC, en assurant l'unicité de l'adresse email.

### Évolutions techniques
- Migration vers Better Auth pour une sécurité renforcée et une gestion des utilisateurs plus robuste.
- Refactorisation importante du code pour la migration vers Kysely, un nouveau moteur de requête SQL, améliorant les performances et la maintenabilité.
- Mise en place d'un nouveau système de réparation des données (ZLV repair harness) pour identifier et corriger les anomalies.
- Amélioration de la gestion des transactions et de la cohérence des données.
- Optimisation des requêtes SQL et de l'utilisation de la base de données.
- Mise à jour des dépendances et correction de vulnérabilités.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la documentation et de la configuration du projet.

### Autres changements
- Ajout de tests Cypress et Playwright pour améliorer la couverture des tests d'intégration.
- Amélioration de la gestion des erreurs et des logs.
- Corrections de style et de formatage du code.
- Mise à jour de la documentation pour refléter les changements apportés.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des variables d'environnement.
- Correction de problèmes de performance et d'optimisation du code.
- Ajout de nouvelles métriques et de tableaux de bord pour suivre l'état du projet.
- Mise en place d'un pipeline CI/CD plus robuste et automatisé.
