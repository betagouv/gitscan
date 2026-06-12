## Changelog : tchap-e2e-playwright (30 derniers jours, au 11 juin 2026)

### Résumé
Ce changelog couvre les dernières améliorations apportées aux tests d'intégration et d'authentification de Tchap. Les efforts se sont concentrés sur l'amélioration de la couverture des tests, notamment pour la fédération, les règles d'accès, l'invitation d'utilisateurs externes et les scénarios de départ de salles. Des refactorings ont également été effectués pour améliorer l'organisation du code et la fiabilité des tests.

### Évolutions fonctionnelles
- Ajout de scénarios de test pour quitter une salle, que celle-ci soit chiffrée ou non. [#44](https://github.com/tchapgouv/tchap-e2e-playwright/issues/44)
- Amélioration des tests liés à l'invitation d'utilisateurs externes et aux niveaux d'autorisation (power levels).
- Ajout de tests pour la mise à niveau de salles. [#47](https://github.com/tchapgouv/tchap-e2e-playwright/issues/47)
- Ajout de tests pour la recherche fédérée. [#44](https://github.com/tchapgouv/tchap-e2e-playwright/issues/44)
- Ajout de la possibilité de spécifier un nom d'affichage lors de la création d'un utilisateur. [#44](https://github.com/tchapgouv/tchap-e2e-playwright/issues/44)
- Ajout de tests pour les règles d'accès via l'API. [#46](https://github.com/tchapgouv/tchap-e2e-playwright/issues/46)
- Ajout de tests de fédération. [#50](https://github.com/tchapgouv/tchap-e2e-playwright/issues/50)
- Ajout de scénarios pour le dernier administrateur d'une salle.

### Évolutions techniques
- Refactorisation du client d'administration MAS. [#52](https://github.com/tchapgouv/tchap-e2e-playwright/issues/52)
- Déplacement des tests API vers un dossier spécifique pour une meilleure organisation.
- Refactorisation des tests pour améliorer la lisibilité et la maintenance.
- Correction de l'URL `EXTERNAL_MAS_URL`.
- Renommage de `BASE_URL` en `MATRIX_URL`.
- Ajout de la variable d'environnement `MAS_ADMIN_URL`.
- Correction du chemin d'accès pour certains tests.
- Suppression d'un test temporairement défaillant.

### Autres changements
- Mise à jour de la documentation.
- Correction de la documentation.
- Organisation des tests d'intégration dans un dossier dédié.
- Correction de l'exécution des tests.
- Refactorisation du test minimal. [#49](https://github.com/tchapgouv/tchap-e2e-playwright/issues/49)
