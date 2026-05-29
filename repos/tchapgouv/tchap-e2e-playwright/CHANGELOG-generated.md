## Changelog : tchap-e2e-playwright (30 derniers jours, au 28 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées aux tests d'intégration et d'authentification de Tchap au cours du dernier mois. Les modifications incluent l'ajout de tests pour les règles d'accès via l'API, l'amélioration des tests d'authentification avec la gestion des noms d'affichage et une réorganisation du code pour une meilleure maintenabilité.

### Évolutions fonctionnelles
- Ajout de tests pour la création d'utilisateurs avec un nom d'affichage, améliorant la couverture des tests d'authentification.  [#44](https://github.com/tchapgouv/tchap-e2e-playwright/issues/44)
- Implémentation de tests d'intégration pour les règles d'accès via l'API. [#46](https://github.com/tchapgouv/tchap-e2e-playwright/issues/46)
- Amélioration des tests d'authentification pour supporter la recherche fédérée. [#44](https://github.com/tchapgouv/tchap-e2e-playwright/issues/44)

### Évolutions techniques
- Réorganisation du code : déplacement des tests d'intégration dans un dossier dédié "integration". [#4576038](https://github.com/tchapgouv/tchap-e2e-playwright/commit/4576038)
- Déplacement du module vers le dossier "synapse" pour une meilleure organisation. [#86e86b1](https://github.com/tchapgouv/tchap-e2e-playwright/commit/86e86b1)
- Correction de problèmes d'exécution des tests en CI, augmentant la fiabilité de la suite de tests. [#1466880](https://github.com/tchapgouv/tchap-e2e-playwright/commit/1466880)
- Correction de bugs dans l'exécution des tests. [#b46d1d2](https://github.com/tchapgouv/tchap-e2e-playwright/commit/b46d1d2)

### Autres changements
- Mise à jour de la documentation et correction de bugs mineurs. [#36d6366](https://github.com/tchapgouv/tchap-e2e-playwright/commit/36d6366)
