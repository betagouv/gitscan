## Changelog : cunningham (30 derniers jours, au 26 avril 2026)

### Résumé
Ce mois-ci, Cunningham a connu des améliorations significatives concernant la modal, avec l'introduction d'un système de variantes pour une plus grande flexibilité. La migration vers GitHub Actions pour le CI/CD a également été finalisée, améliorant ainsi la sécurité et l'efficacité du processus de publication. Des corrections d'accessibilité ont été apportées aux composants Toast et Dropdown.

### Évolutions fonctionnelles
- Ajout d'un système de variantes pour le composant Modal, offrant des mises en page par défaut et en onglets. [#issue à retrouver]
- Extraction du calendrier en tant que composant autonome. [#issue à retrouver]
- Correction du comportement du bouton "désactivé" dans les liens du composant Button. [#89a91e6](https://github.com/suitenumerique/cunningham/commit/89a91e6)
- Amélioration de l'accessibilité du bouton de bascule du menu déroulant avec un nom accessible correct. [#5c715fd](https://github.com/suitenumerique/cunningham/commit/5c715fd)
- Amélioration de l'accessibilité du composant Toast en masquant l'icône décorative des lecteurs d'écran. [#1f28aeb](https://github.com/suitenumerique/cunningham/commit/1f28aeb)

### Évolutions techniques
- Migration du système d'intégration continue (CI) de CircleCI vers GitHub Actions pour une meilleure sécurité et flexibilité. [#c31ebd9](https://github.com/suitenumerique/cunningham/commit/c31ebd9)
- Utilisation de NPM Trusted Publisher pour la publication des packages, renforçant la sécurité de la chaîne d'approvisionnement. [#54c3e65](https://github.com/suitenumerique/cunningham/commit/54c3e65)
- Refactoring du formatage dans les composants Select et Modal. [#3615ff8](https://github.com/suitenumerique/cunningham/commit/3615ff8)
- Refactorisation des tokens de formulaire et mise à jour du composant Modal. [#5c86834](https://github.com/suitenumerique/cunningham/commit/5c86834)
- Publication de la version 4.3.0. [#1f6a938](https://github.com/suitenumerique/cunningham/commit/1f6a938)

### Autres changements
- Régénération des fichiers de tokens. [#15b8575](https://github.com/suitenumerique/cunningham/commit/15b8575) et [#d9f569f](https://github.com/suitenumerique/cunningham/commit/d9f569f)
