## Changelog : tchap-e2e-playwright (30 derniers jours, au 4 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées aux tests d'intégration et d'authentification de Tchap au cours du dernier mois. Les efforts se sont concentrés sur l'ajout de tests pour la fédération, les règles d'accès, la création d'utilisateurs et l'amélioration de la robustesse de l'exécution des tests en CI.

### Évolutions fonctionnelles
- Ajout de tests pour la fédération, permettant de vérifier le bon fonctionnement de l'interconnexion avec d'autres serveurs Matrix. [#50](https://github.com/tchapgouv/tchap-e2e-playwright/issues/50)
- Amélioration des tests de création d'utilisateurs : ajout de la possibilité de spécifier un nom d'affichage lors de la création d'un utilisateur, et ajout d'un scénario pour la recherche fédérée. [#44](https://github.com/tchapgouv/tchap-e2e-playwright/issues/44)
- Ajout de tests d'intégration pour les règles d'accès via l'API. [#46](https://github.com/tchapgouv/tchap-e2e-playwright/issues/46)
- Ajout d'un test pour la mise à niveau d'une salle. [#47](https://github.com/tchapgouv/tchap-e2e-playwright/issues/47)

### Évolutions techniques
- Refactorisation des tests minimaux pour une meilleure maintenabilité. [#49](https://github.com/tchapgouv/tchap-e2e-playwright/issues/49)
- Déplacement des tests d'intégration vers un dossier dédié `integration` pour une meilleure organisation du code.
- Correction de problèmes d'exécution des tests.
- Augmentation du nombre de tentatives en CI pour améliorer la stabilité des tests.

### Autres changements
- Correction de la documentation.
- Correction de tests et de la documentation.
