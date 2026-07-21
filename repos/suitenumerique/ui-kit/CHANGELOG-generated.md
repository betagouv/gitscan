## Changelog : ui-kit (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à plusieurs composants, notamment le filtre, le menu utilisateur, et introduit de nouveaux composants comme le SmartScroller et le StorageGauge. L'accessibilité a été améliorée sur plusieurs éléments, et des corrections de bugs ont été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout du composant `StorageGauge` pour afficher l'utilisation du stockage, avec des stories et des tests associés.
- Amélioration du composant `SearchFilter` avec l'ajout d'une ligne de réinitialisation et la possibilité d'ajouter des sous-éléments personnalisés.
- Ajout d'une option pour masquer la vue mobile du menu utilisateur via la prop `withMobileView`.
- Ajout du composant `HelpMenu` avec des options pour les liens légaux, les options personnalisées et les liens `mailto`.
- Ajout du composant `SmartScroller` pour un défilement fluide.
- Centrage des boutons du modal sur mobile pour une meilleure lisibilité.
- Amélioration de l'accessibilité du menu utilisateur.
- Ajout d'un indicateur visuel pour le focus clavier dans les options du filtre.

### Évolutions techniques
- Refactorisation du composant `MenuItemBody` pour le réutiliser dans différents menus (dropdown, menu contextuel, filtre).
- Suppression du code inutilisé `lockedContent` du composant `StorageGaugeInformation`.
- Amélioration de la gestion des couleurs du `StorageGauge` via des classes de modificateurs.
- Extraction de la ligne de réinitialisation du filtre dans un composant partagé.
- Mise à jour des icônes depuis Figma.
- Amélioration de la performance du `SmartScroller` en maintenant les flèches montées pour des transitions fluides.
- Correction d'un problème de comportement du panneau de filtre qui se fermait au survol au lieu d'un clic.
- Correction d'un bug empêchant le drag-and-drop dans l'arborescence (tree-view).
- Amélioration de la gestion des événements pour le menu contextuel afin d'éviter des sélections fantômes.

### Autres changements
- Ajout de documentation pour le composant `HelpMenu`.
- Ajout de tests E2E pour le `StorageGauge` et le `HelpMenu`.
- Traduction du placeholder par défaut du `UserSearchFilter` en allemand et espagnol.
- Ajout de catégories de documentation pour `lasuite/docs`.
- Augmentation du timeout sur un test spécifique.
- Ajout de traductions allemandes et espagnoles pour le composant `LaGaufreV2`.
- Ajout de tests pour couvrir le comportement de fermeture du sous-panneau du filtre.
- Correction de l'export des fichiers d'icônes.
- Ajout de tests Playwright pour les composants.
