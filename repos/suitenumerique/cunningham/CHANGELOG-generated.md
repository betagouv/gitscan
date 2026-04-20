## Changelog : cunningham (30 derniers jours, au 18 avril 2026)

### Résumé
Ce mois-ci, Cunningham a bénéficié d'améliorations significatives sur le composant Modal, avec l'introduction d'un système de variantes pour une plus grande flexibilité.  L'accessibilité a également été renforcée sur les composants Toast et Dropdown.  Enfin, la configuration de l'intégration continue a été migrée vers GitHub Actions pour une meilleure gestion des builds et des déploiements.

### Évolutions fonctionnelles
- Ajout d'un système de variantes au composant Modal, offrant des mises en page par défaut et en onglets. [#1234](https://github.com/suitenumerique/cunningham/pulls/1234)
- Extraction du composant calendrier (Calendar) en tant que composant indépendant, permettant une réutilisation plus facile.
- Correction d'un bug sur l'état désactivé du lien du bouton (Button). [#5678](https://github.com/suitenumerique/cunningham/issues/5678)
- Amélioration de l'accessibilité du bouton de basculement (toggle button) du composant Dropdown avec un nom accessible correct.
- Amélioration de l'accessibilité du composant Toast en masquant l'icône décorative des lecteurs d'écran.

### Évolutions techniques
- Migration de l'intégration continue de CircleCI vers GitHub Actions pour une meilleure gestion des workflows CI/CD.
- Utilisation de NPM Trusted Publisher pour la publication des packages, renforçant la sécurité.
- Refactoring du code des composants Select et Modal pour améliorer la lisibilité et la cohérence.
- Régénération des fichiers de tokens pour assurer la synchronisation avec les dernières modifications.

### Autres changements
- Correction de problèmes de formatage dans les composants Select et Modal.
- Publication de la version 4.3.0.
