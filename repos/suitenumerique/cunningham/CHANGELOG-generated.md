## Changelog : cunningham (30 derniers jours, au 27 avril 2026)

### Résumé
Cette version apporte des améliorations significatives au composant Modal, avec l'introduction d'un système de variantes pour une plus grande flexibilité.  La migration vers GitHub Actions pour la CI/CD améliore la sécurité et la fiabilité du processus de publication. Une correction a été apportée à l'état désactivé des liens dans le composant Button.

### Évolutions fonctionnelles
- **Modal :** Ajout d'un système de variantes avec des mises en page par défaut et onglets, offrant plus de contrôle sur l'apparence et le comportement du composant.
- **Button :** Correction d'un bug concernant l'état désactivé des liens [#89a91e6](https://github.com/suitenumerique/cunningham/commit/89a91e6).
- **Calendar :** Extraction du calendrier en tant que composant indépendant, facilitant sa réutilisation et son adaptation.

### Évolutions techniques
- **CI/CD :** Migration de CircleCI vers GitHub Actions pour une meilleure sécurité et une gestion simplifiée des workflows.
- **Publication :** Utilisation de NPM Trusted Publisher pour sécuriser la publication des packages.
- **Refactoring :** Refactorisation des tokens de formulaire et mise à jour des composants Select et Modal pour une meilleure cohérence et maintenabilité.

### Autres changements
- Régénération des fichiers de tokens.
- Amélioration du formatage dans les composants Select et Modal.
- Publication de la version 4.3.0 du projet [#1f6a938](https://github.com/suitenumerique/cunningham/commit/1f6a938).
