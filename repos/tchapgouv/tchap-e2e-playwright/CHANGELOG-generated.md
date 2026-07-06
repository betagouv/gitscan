## Changelog : tchap-e2e-playwright (30 derniers jours, au 04 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la couverture des tests, notamment concernant la rétention des salons publics, l'invitation d'utilisateurs externes, les restrictions d'accès et les tests de l'API. Des refactorings ont également été effectués pour optimiser le code et améliorer sa structure.

### Évolutions fonctionnelles
- Ajout de tests pour la rétention des salons publics. [#56](https://github.com/tchapgouv/tchap-e2e-playwright/issues/56)
- Ajout de scénarios de test pour quitter un salon, qu'il soit chiffré ou non.
- Ajout de tests pour l'invitation d'utilisateurs externes et la gestion des niveaux d'administration (power levels).
- Ajout de tests pour les restrictions de recherche externes.
- Ajout de scénarios pour le dernier administrateur d'un salon.
- Amélioration des tests existants avec l'ajout d'attentes pour les messages.
- Adaptation des tests minimaux avec les règles d'accès et le nouveau flux avec un environnement externe.

### Évolutions techniques
- Refactoring du client d'administration MAS [#52](https://github.com/tchapgouv/tchap-e2e-playwright/issues/52) pour améliorer sa maintenabilité.
- Optimisation générale du code. [#54](https://github.com/tchapgouv/tchap-e2e-playwright/issues/54)
- Déplacement des tests API vers un dossier spécifique pour une meilleure organisation.
- Renommage de la variable `BASE_URL` en `MATRIX_URL` pour plus de clarté.
- Ajout de la variable `MAS_ADMIN_URL` pour configurer l'URL de l'administration MAS.
- Correction du chemin d'accès à l'API.
- Correction de l'URL `EXTERNAL_MAS_URL`.

### Autres changements
- Déplacement des informations d'identification vers un fichier de secrets pour une meilleure sécurité. [#53](https://github.com/tchapgouv/tchap-e2e-playwright/issues/53)
- Suppression temporaire d'un test en échec.
- Ajout d'un second appel dans un test.
