## Changelog : cunningham (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, Cunningham a bénéficié d'améliorations significatives sur ses composants Modale et Calendrier, avec l'introduction de nouveaux systèmes de variantes pour la Modale.  L'infrastructure de CI/CD a également été modernisée en migrant vers GitHub Actions pour une meilleure gestion des builds et des déploiements. Des corrections d'accessibilité ont été apportées aux composants Toast et Dropdown.

### Évolutions fonctionnelles
- **Modale :** Ajout d'un système de variantes permettant de définir différents agencements (layouts) par défaut et avec onglets. [#issue à retrouver]
- **Calendrier :** Extraction du composant calendrier en tant que composant autonome, facilitant sa réutilisation. [#issue à retrouver]
- **Bouton :** Correction d'un bug empêchant le désactivation correcte des liens de boutons. [#89a91e6](https://github.com/suitenumerique/cunningham/commit/89a91e6)
- **Dropdown :** Amélioration de l'accessibilité du bouton de bascule (toggle) du dropdown en définissant un nom accessible approprié. [#issue à retrouver]
- **Toast :** Amélioration de l'accessibilité des notifications Toast en masquant l'icône décorative des lecteurs d'écran. [#issue à retrouver]

### Évolutions techniques
- **CI/CD :** Migration de l'infrastructure d'intégration continue depuis CircleCI vers GitHub Actions pour une meilleure intégration avec l'écosystème GitHub. [#issue à retrouver]
- **Sécurité :** Utilisation de NPM Trusted Publisher pour sécuriser la publication des paquets. [#issue à retrouver]
- **Refactoring :** Refactorisation des tokens de formulaire et mise à jour des composants Select et Modal pour une meilleure cohérence et maintenabilité. [#issue à retrouver]
- **Tokens :** Régénération des fichiers de tokens pour assurer la cohérence du design system. [#issue à retrouver]

### Autres changements
- Publication de la version 4.3.0. [#1f6a938](https://github.com/suitenumerique/cunningham/commit/1f6a938)
- Nettoyage et amélioration du formatage dans les composants Select et Modal. [#3615ff8](https://github.com/suitenumerique/cunningham/commit/3615ff8)
