## Changelog : ui-kit (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à plusieurs composants clés, notamment le filtre, le menu utilisateur et l'affichage de l'espace de stockage. De nouveaux composants comme le SmartScroller et le HelpMenu ont été ajoutés, enrichissant la bibliothèque d'outils disponibles pour les développeurs. L'accessibilité a également été améliorée sur plusieurs éléments.

### Évolutions fonctionnelles
- Ajout d'un composant "SmartScroller" pour un défilement amélioré.
- Ajout d'un composant "HelpMenu" permettant d'intégrer des liens d'aide légaux, personnalisés et des liens par email.
- Amélioration du filtre : ajout d'une option de réinitialisation et support de sous-éléments personnalisés.
- Amélioration du menu utilisateur : ajout d'une prop pour masquer la vue mobile et amélioration de l'accessibilité.
- Amélioration de l'accessibilité du composant "StorageGauge" (indicateur d'espace de stockage).
- Centrage des boutons dans les modales sur mobile.
- Ajout de catégories de documents pour "lasuite/docs".
- Rafraîchissement des icônes de fichiers miniatures.
- Ajout de traductions allemandes et espagnoles pour le menu "Ouvrir dans une nouvelle fenêtre".

### Évolutions techniques
- Refactorisation du composant "MenuItem" avec l'extraction d'un composant "MenuItemBody" partagé.
- Suppression du code inutilisé "lockedContent" du composant "StorageGaugeInformation".
- Utilisation de classes de modificateurs pour contrôler la couleur de remplissage du "StorageGauge".
- Mise à jour de la bibliothèque d'icônes à partir de la source Figma.
- Amélioration de la gestion des événements pour le composant "ContextMenu" afin d'éviter des comportements inattendus.
- Correction d'un problème empêchant le drag-and-drop dans la vue arborescente.
- Amélioration de la performance du "SmartScroller" en maintenant les flèches montées.

### Autres changements
- Ajout de tests E2E pour le "StorageGauge", le "HelpMenu" et le comportement de fermeture du sous-panneau de filtre.
- Ajout de stories et de documentation pour le "StorageGauge", le "SmartScroller" et le "HelpMenu".
- Correction de problèmes de focus clavier dans les options du filtre.
- Correction de bugs mineurs liés à l'affichage et au style de certains composants.
- Augmentation du timeout sur un test spécifique.
- Ajout de tests Playwright pour la couverture des composants.
- Mise à jour des dépendances.
