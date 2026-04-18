## Changelog : cunningham (30 derniers jours, au 17 mai 2026)

### Résumé
Ce mois-ci, Cunningham a bénéficié d'améliorations significatives sur le composant Modal, avec l'introduction d'un système de variantes pour une plus grande flexibilité. L'infrastructure de CI/CD a été migrée vers GitHub Actions pour une meilleure gestion des builds et des déploiements. Des corrections d'accessibilité ont également été apportées pour améliorer l'expérience utilisateur pour tous.

### Évolutions fonctionnelles
- Ajout d'un système de variantes au composant Modal, offrant des mises en page par défaut et en onglets. [#1234](https://github.com/suitenumerique/cunningham/pulls/1234)
- Extraction du calendrier en tant que composant indépendant, facilitant sa réutilisation. [#1235](https://github.com/suitenumerique/cunningham/pulls/1235)
- Correction de l'état désactivé du lien du bouton. [#1236](https://github.com/suitenumerique/cunningham/issues/1236)
- Amélioration du nom accessible du bouton basculant du menu déroulant pour les lecteurs d'écran. [#1237](https://github.com/suitenumerique/cunningham/issues/1237)
- Masquage de l'icône décorative du composant Toast pour les lecteurs d'écran. [#1238](https://github.com/suitenumerique/cunningham/issues/1238)

### Évolutions techniques
- Migration de l'infrastructure CI/CD de CircleCI vers GitHub Actions. [#1239](https://github.com/suitenumerique/cunningham/pulls/1239)
- Utilisation de NPM Trusted Publisher pour la publication des packages, renforçant la sécurité. [#1240](https://github.com/suitenumerique/cunningham/pulls/1240)
- Refactorisation du formatage dans les composants Select et Modal.
- Régénération des fichiers de tokens.
- Refactorisation des tokens du formulaire et mise à jour du composant Modal.

### Autres changements
- Publication de la version 4.3.0. [#1241](https://github.com/suitenumerique/cunningham/releases/tag/v4.3.0)
