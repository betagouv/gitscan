## Changelog : tchap-e2e-playwright (30 derniers jours, au 2026-05-13)

### Résumé
Ce changelog couvre les améliorations apportées aux tests d'authentification et de création de salles pour le service Tchap. Les modifications incluent la correction de bugs, la mise à jour des dépendances et l'amélioration de la robustesse des tests en environnement CI.

### Évolutions fonctionnelles
- Correction du test de déconnexion pour assurer son bon fonctionnement. [#40](https://github.com/tchapgouv/tchap-e2e-playwright/issues/40)
- Correction de la création de salle, résolvant un problème rencontré lors des tests. [#40](https://github.com/tchapgouv/tchap-e2e-playwright/issues/40)
- Mise à jour du code de vérification dans les tests pour refléter les changements récents.

### Évolutions techniques
- Mise à jour des dépendances, notamment Playwright, vers la version `v1.59.1-noble` pour bénéficier des dernières corrections et améliorations. [#38](https://github.com/tchapgouv/tchap-e2e-playwright/issues/38)
- Déplacement d'un module dans le dossier `synapse` pour une meilleure organisation du code.
- Ajout de l'intégration `int02`.
- Augmentation du nombre de tentatives en CI pour améliorer la stabilité des tests.

### Autres changements
- Aucun changement significatif à signaler dans cette catégorie.
