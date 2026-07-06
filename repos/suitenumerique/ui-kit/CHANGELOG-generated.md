## Changelog : ui-kit (30 derniers jours, au 3 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la recherche et au filtrage, avec l'ajout de composants pour réinitialiser les filtres et un composant "SmartScroller" pour une navigation fluide. Des corrections d'accessibilité et des améliorations visuelles ont également été apportées, notamment au menu utilisateur et aux modales. Enfin, de nouvelles icônes ont été générées à partir de Figma.

### Évolutions fonctionnelles
- Ajout d'une option pour réinitialiser les filtres dans les composants `Filter` et `SearchFilter`.
- Implémentation du composant `SmartScroller` pour une navigation améliorée dans les listes longues.
- Ajout d'un support pour les sous-éléments personnalisés dans le composant `Filter`.
- Amélioration de l'accessibilité du menu utilisateur avec des attributs ARIA appropriés.
- Ajout d'une option pour masquer la vue mobile du menu utilisateur via la prop `withMobileView`.
- Ajout d'un menu d'aide (`HelpMenu`) avec des liens légaux et des options personnalisées.
- Centrage du contenu des boutons des modales sur mobile.
- Ajout d'une option pour ouvrir les liens dans une nouvelle fenêtre avec un label accessible.

### Évolutions techniques
- Refactorisation du composant `MenuItem` pour réutiliser le composant `MenuItemBody`.
- Extraction du composant de réinitialisation de ligne dans un composant partagé.
- Mise à jour des icônes à partir de la source Figma.
- Amélioration de la gestion du focus clavier dans les options du filtre de recherche.
- Correction d'un problème empêchant le drag-and-drop dans la vue arborescente (`TreeView`).
- Correction d'un bug dans la modale qui empêchait la fermeture correcte au survol.
- Amélioration de la performance du composant `SmartScroller` en maintenant les flèches montées.

### Autres changements
- Ajout de traductions allemandes et espagnoles pour le label de nouvelle fenêtre du menu.
- Ajout d'une catégorie "docs" pour les fichiers de documentation LaSuite numérique.
- Ajout de tests E2E pour le composant `HelpMenu` et le comportement de la fermeture du sous-panneau de filtre.
- Ajout d'un effet de survol sur la poignée de redimensionnement du panneau.
- Correction de problèmes liés à la modale de recherche.
- Correction de l'utilisation de `currentColor` pour le remplissage des SVG dans `LaGaufreV2`.
- Utilisation de la balise `<header>` au lieu de `<div>` pour l'en-tête dans la mise en page, améliorant ainsi l'accessibilité.
