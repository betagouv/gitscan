## Changelog : ui-kit (30 derniers jours, au 23 juin 2026)

### Résumé
Les dernières mises à jour du kit d'interface utilisateur se concentrent sur l'amélioration de l'accessibilité, l'ajout de traductions pour l'allemand et l'espagnol, ainsi que des corrections de bugs et des améliorations visuelles mineures. Une nouvelle fonctionnalité permet d'indiquer si un lien dans un menu s'ouvre dans une nouvelle fenêtre, avec une étiquette d'accessibilité appropriée.

### Évolutions fonctionnelles
- Ajout d'une indication visuelle et textuelle pour les liens de menu ouvrant une nouvelle fenêtre, améliorant l'expérience utilisateur et l'accessibilité. [#246](https://github.com/suitenumerique/ui-kit/issues/246)
- Amélioration visuelle : ajout d'un effet de survol sur la poignée de redimensionnement des panneaux.
- Correction de problèmes liés à la modale de recherche.
- Amélioration du rendu des icônes SVG avec `currentColor`.
- Utilisation de balises `<header>` sémantiques au lieu de `<div>` pour les en-têtes, améliorant l'accessibilité.
- Mise à jour de la bibliothèque d'icônes.

### Évolutions techniques
- Ajout de traductions en allemand (de-DE) et en espagnol (es-ES) pour le composant Gaufre. [#242](https://github.com/suitenumerique/ui-kit/issues/242)
- Mise à jour de la version du package.

### Autres changements
- Ajout de stories pour le composant "OpensInNewWindow" du menu déroulant.
- Correction de typos et amélioration de la documentation.
- Mise à jour de la dépendance `cunningham-react` vers la version 4.2.0.
- Amélioration de la visibilité de l'option de suppression dans le menu déroulant des rôles d'accès.
- Corrections de style sur le menu utilisateur et la modale de partage.
- Suppression d'importations de styles inutilisées.
