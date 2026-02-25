## Changelog : mle-back (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la recherche de logements, notamment l'ajout de critères de prix, l'intégration de nouvelles sources de données (SAIEM Dragouignan, Cardinal Campus, Logis Métropole, ACM Habitat), et l'amélioration de la pertinence des résultats. Des fonctionnalités de notification ont été ajoutées, ainsi qu'un suivi des événements via Matomo pour mieux comprendre l'utilisation de l'application. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance du backend.

### Évolutions fonctionnelles
- Ajout de filtres de prix minimum et maximum dans la recherche de logements (#38b7682).
- Intégration de la source de logements SAIEM Dragouignan (#3574821).
- Intégration de la source de logements Cardinal Campus (#fbef5a3).
- Intégration de la source de logements Logis Métropole (#9eacf0e).
- Intégration de la source de logements ACM Habitat (#0d23ae2).
- Ajout de la possibilité d'ajouter une image lors de la création d'un logement (#f5c2c71).
- Ajout d'une fonctionnalité de notification pour informer les utilisateurs des nouvelles offres (#2583247).
- Ajout du nombre d'alertes pour l'utilisateur (#2d0854e).
- Ajout d'un service de gestion des villes (#6f4a589).
- Ajout du champ "wifi" aux logements (#778eb69).
- Amélioration du classement des logements dans les résultats de recherche (#c0949ff).

### Évolutions techniques
- Mise en place d'un suivi des événements via Matomo pour l'analyse de l'utilisation (#3e99f65).
- Refactorisation du code pour améliorer la qualité et la maintenabilité (#f09a9c1).
- Amélioration de la recherche avec l'utilisation de FTS et de trigrammes (#0d6bff9).
- Utilisation de contraintes de base de données pour garantir l'unicité de l'adresse email des utilisateurs (#f58cb4d).
- Mise à jour des dépendances : Ruff (0.14.10 -> 0.14.11 -> 0.14.13 -> 0.15.0), Sentry SDK (2.48.0 -> 2.49.0 -> 2.50.0 -> 2.51.0 -> 2.52.0), djangorestframework-stubs (3.16.6 -> 3.16.7).
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code (#2352def).
- Amélioration de la gestion des variables d'environnement (#a32c2e9).

### Autres changements
- Correction de bugs liés à l'export Excel, notamment l'affichage de la disponibilité et des prix (#c831251, #d86b071).
- Correction de problèmes d'URL pour les images (#ea50a3e, #e6c0926).
- Ajout d'un script pour importer les prix du CROUS (#d37f968).
- Ajout d'un fichier de verrouillage pour les dépendances (#c5a4245).
- Suppression de code inutile (#707177b, #67541d0).
- Amélioration des messages de notification (#47dfda4).
- Correction de bugs et amélioration des tests (#242af63, #5a3e4d7, #df28500, #d3f16ff, #f955c00, #6008e6b, #38a5f05).
