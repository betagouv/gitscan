## Changelog : mission-transition-ecologique-back (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des données "canoniques" (données de référence) des programmes de transition écologique, avec notamment la persistance de ces données et la création de packages pour faciliter leur utilisation. Des optimisations de la chaîne CI/CD ont également été apportées pour accélérer les tests et les déploiements. Enfin, des fonctionnalités liées à l'export de données et à l'intégration de l'IA ont été ajoutées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données "agir" via l'API, en provenance des données canoniques. [#48](https://github.com/betagouv/mission-transition-ecologique-back/issues/48)
- Implémentation d'une nouvelle compétence "worktree-init" pour l'IA. [#44](https://github.com/betagouv/mission-transition-ecologique-back/issues/44)
- Persistance des programmes publiés dans un espace de stockage canonique dédié.
- Amélioration de l'aspect visuel avec un design type DSFR. [#3](https://github.com/betagouv/mission-transition-ecologique-back/issues/3)

### Évolutions techniques
- Création de packages pour les adaptateurs de format de données, permettant de garantir la qualité des données au format canonique. [#48](https://github.com/betagouv/mission-transition-ecologique-back/issues/48)
- Mise en place d'un package "canonical" pour centraliser la gestion des données canoniques. [#33](https://github.com/betagouv/mission-transition-ecologique-back/issues/33)
- Optimisation de la chaîne CI/CD : parallélisation des jobs, mise en cache de Playwright/Nx et des tests end-to-end pour les builds de production. [#42](https://github.com/betagouv/mission-transition-ecologique-back/issues/42)
- Correction des spécifications des tests end-to-end et configuration des commandes de test.
- Configuration du projet avec Claude Code (règles de commentaires et hooks). [#41](https://github.com/betagouv/mission-transition-ecologique-back/issues/41)

### Autres changements
- Correction automatique du fichier `tsconfig.lib.json` pour le formatage des adaptateurs (nx).
