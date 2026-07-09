## Changelog : ui-kit (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'accessibilité, notamment pour le composant StorageGauge et le menu utilisateur. De nouveaux composants ont été ajoutés, comme SmartScroller et HelpMenu, enrichissant la bibliothèque. Des corrections de bugs et des optimisations ont été apportées pour améliorer l'expérience utilisateur et la stabilité du code.

### Évolutions fonctionnelles
- Ajout du composant `StorageGauge` pour afficher l'utilisation du stockage, avec des améliorations d'accessibilité.
- Ajout d'une option pour masquer la vue mobile du menu utilisateur via la prop `withMobileView`.
- Ajout d'un bouton de réinitialisation au filtre et à la recherche filtrée.
- Ajout du composant `SmartScroller` pour un défilement plus fluide.
- Ajout du composant `HelpMenu` avec support pour des liens légaux et des options personnalisées.
- Amélioration de l'accessibilité du menu utilisateur avec des labels ARIA pour les liens ouvrant une nouvelle fenêtre.
- Centrage du contenu des boutons des modales sur mobile.
- Effet de survol sur la poignée de redimensionnement du panneau.
- Correction de problèmes de positionnement de LaGaufreV2.

### Évolutions techniques
- Refactorisation du code pour améliorer la réutilisation des composants `MenuItemBody`.
- Extraction du composant `reset row` en un composant partagé.
- Utilisation de classes de modificateur pour la couleur de remplissage du `gauge`.
- Amélioration de la gestion des événements pour le panneau `SmartScroller` afin d'éviter des problèmes de flou.
- Mise à jour de la bibliothèque d'icônes à partir de Figma.
- Suppression des règles `pointer-events` qui perturbaient le drag-and-drop dans l'arborescence.
- Ajout de tests E2E pour les nouveaux composants et les fonctionnalités améliorées.
- Correction d'un bug empêchant la fermeture du sous-panneau de filtre sur clic extérieur.

### Autres changements
- Traduction du placeholder par défaut du filtre utilisateur en différentes langues.
- Ajout d'une catégorie de documentation "docs" pour lasuite/docs.
- Ajout de traductions allemandes et espagnoles pour le menu.
- Ajout de stories et de documentation pour les nouveaux composants.
- Correction de problèmes de style dans le menu utilisateur.
- Amélioration de la gestion des tests et des timeouts.
- Ajout de tests Playwright pour la couverture des composants.
- Correction de bugs mineurs et améliorations de la qualité du code.
