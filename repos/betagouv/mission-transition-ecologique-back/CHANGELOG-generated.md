## Changelog : mission-transition-ecologique-back (30 derniers jours, au 27 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la qualité des données, notamment via la persistance des programmes publiés dans un espace de stockage "canonique". Des optimisations de la chaîne CI/CD ont également été apportées pour accélérer les tests et les déploiements. Enfin, des améliorations de l'interface utilisateur ont été initiées avec l'intégration d'éléments de design similaires à DSFR.

### Évolutions fonctionnelles
- Implémentation d'un stockage "canonique" pour les programmes publiés, assurant une meilleure qualité des données. [#33](https://github.com/betagouv/mission-transition-ecologique-back/issues/33)
- Création d'un package pour les adaptateurs de format et réexportation de la TEE pour confirmer la qualité des données au format canonique. [#48](https://github.com/betagouv/mission-transition-ecologique-back/issues/48)
- Début de l'intégration d'éléments de design de type DSFR pour améliorer l'interface utilisateur. [#3](https://github.com/betagouv/mission-transition-ecologique-back/issues/3)

### Évolutions techniques
- Parallélisation des jobs CI, et mise en cache de Playwright/Nx et des tests e2e pour accélérer la chaîne de production. [#42](https://github.com/betagouv/mission-transition-ecologique-back/issues/42)
- Ajout de tests unitaires, d'intégration et e2e au pipeline CI/CMS. [#42](https://github.com/betagouv/mission-transition-ecologique-back/issues/42)
- Correction des spécifications des tests e2e et configuration des commandes de test. [#42](https://github.com/betagouv/mission-transition-ecologique-back/issues/42)
- Configuration de Claude Code pour le projet, incluant une règle de commentaire et des hooks. [#41](https://github.com/betagouv/mission-transition-ecologique-back/issues/41)

### Autres changements
- Aucun changement significatif à signaler.
