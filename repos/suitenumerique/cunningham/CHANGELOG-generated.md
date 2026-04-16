## Changelog : cunningham (30 derniers jours, au 30 mars 2026)

### Résumé
Cette version apporte des améliorations significatives à la modal, avec l'introduction d'un système de variantes pour une plus grande flexibilité. Des composants ont été extraits et refactorisés pour une meilleure réutilisabilité et maintenabilité.  L'accessibilité a également été améliorée, notamment pour les toasts et les boutons de déclenchement de menus déroulants. Enfin, la configuration de l'intégration continue a été migrée vers GitHub Actions pour une meilleure gestion des builds et des déploiements.

### Évolutions fonctionnelles
- **Modal :** Ajout d'un système de variantes permettant de personnaliser l'apparence et le comportement de la modal, avec des mises en page par défaut et en onglets.
- **Calendar :** Extraction du composant calendrier en tant que composant autonome, facilitant sa réutilisation dans d'autres parties de l'application.

### Évolutions techniques
- **CI/CD :** Migration de l'intégration continue de CircleCI vers GitHub Actions pour une meilleure intégration avec l'écosystème GitHub. [#c31ebd9](https://github.com/suitenumerique/cunningham/commit/c31ebd9)
- **Publication :** Utilisation de NPM Trusted Publisher pour sécuriser la publication des packages. [#54c3e65](https://github.com/suitenumerique/cunningham/commit/54c3e65)
- **Refactoring :** Refactorisation des tokens de formulaire et de la base du calendrier. [#5c86834](https://github.com/suitenumerique/cunningham/commit/5c86834)
- **Formatage :** Correction du formatage dans les composants Select et Modal. [#3615ff8](https://github.com/suitenumerique/cunningham/commit/3615ff8)
- **Génération de tokens :** Régénération des fichiers de tokens. [#15b8575](https://github.com/suitenumerique/cunningham/commit/15b8575) et [#d9f569f](https://github.com/suitenumerique/cunningham/commit/d9f569f)

### Autres changements
- **Accessibilité :**
    - Masquage de l'icône décorative des toasts aux lecteurs d'écran. [#1f28aeb](https://github.com/suitenumerique/cunningham/commit/1f28aeb)
    - Correction du nom accessible du bouton de déclenchement du menu déroulant. [#5c715fd](https://github.com/suitenumerique/cunningham/commit/5c715fd)
- **Version :** Publication de la version 4.3.0. [#1f6a938](https://github.com/suitenumerique/cunningham/commit/1f6a938)
