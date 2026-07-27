## Changelog : ui-kit (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur avec l'ajout de nouveaux composants pour la gestion des fichiers et l'affichage de l'espace de stockage. Des améliorations d'accessibilité et des corrections de bugs ont également été implémentées pour améliorer la robustesse et l'ergonomie de la bibliothèque.

### Évolutions fonctionnelles
- Ajout d'une famille de composants pour la gestion des téléchargements de fichiers. [#264](https://github.com/suitenumerique/ui-kit/issues/264)
- Ajout d'un composant `StorageGauge` pour visualiser l'utilisation de l'espace de stockage, incluant des stories et des tests.
- Amélioration du menu utilisateur avec une meilleure adaptation mobile et des améliorations d'accessibilité. [#265](https://github.com/suitenumerique/ui-kit/issues/265)
- Ajout d'une option pour masquer la vue mobile du menu utilisateur via la prop `withMobileView`.
- Ajout d'une option de réinitialisation aux filtres et aux champs de recherche.
- Ajout d'un composant `HelpMenu` avec support pour des liens légaux, des options personnalisées et des liens par email.
- Ajout d'un composant `SmartScroller` pour un défilement plus fluide et optimisé.
- Centrage du contenu des boutons des modales sur mobile.
- Mise à jour des icônes du kit pour correspondre aux dernières spécifications Figma.

### Évolutions techniques
- Stabilisation des tests de composants Storybook.
- Refactorisation du composant `UserMenu` pour une meilleure structure et adaptation.
- Suppression du code inutilisé `lockedContent` de `StorageGaugeInformation`.
- Utilisation de classes de modificateurs pour contrôler la couleur de remplissage du `StorageGauge`.
- Extraction du composant `MenuItemBody` pour une réutilisation accrue dans les menus.
- Amélioration de la gestion des événements pour éviter les comportements inattendus dans le menu contextuel.
- Génération automatique des icônes à partir de Figma.
- Refactorisation du composant `Dropdown` pour améliorer sa flexibilité.

### Autres changements
- Ajout de documentation pour le composant `HelpMenu`.
- Ajout de tests E2E pour le composant `StorageGauge` et le `HelpMenu`.
- Correction d'un bug empêchant la visibilité du focus clavier dans les options du filtre de recherche.
- Correction d'un bug lié à la gestion des événements de survol et de clic sur le panneau de filtre.
- Augmentation du timeout sur un test spécifique pour améliorer sa fiabilité.
- Traduction du placeholder par défaut du filtre utilisateur en allemand et en espagnol.
- Correction d'un problème empêchant le drag-and-drop dans l'arborescence.
- Correction de problèmes de style dans le menu utilisateur.
- Suppression de règles `pointer-events` cassant le drag-and-drop.
