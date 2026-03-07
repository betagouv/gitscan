## Changelog : ui-kit (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées au kit d'interface utilisateur. Les modifications incluent des corrections de style et d'accessibilité sur le menu utilisateur, des ajustements de design sur le composant de partage, et des corrections de typographie et de traductions. Une mise à jour de la librairie Cunningham a également été effectuée.

### Évolutions fonctionnelles
- Amélioration du style et de l'accessibilité du menu utilisateur. [#175](https://github.com/suitenumerique/ui-kit/issues/175)
- Correction de l'affichage du padding du menu utilisateur.
- Correction de la visibilité de l'option de suppression dans le menu de gestion des accès.
- Amélioration du composant de partage avec des informations plus complètes et une conformité accrue aux maquettes Figma.
- Ajout de la propriété `can_delete` et amélioration de la documentation Storybook du composant de partage.
- Ajout du composant `ReleaseNoteModal`.
- Déplacement de la gestion des accès dans le composant `AccessRoleDropdown`.

### Évolutions techniques
- Remplacement des images SVG par des composants React pour les icônes du bouton de partage, améliorant ainsi la maintenabilité et la performance.
- Utilisation du composant `Button` de Cunningham pour le dropdown des rôles d'accès.
- Suppression d'imports de styles Cunningham inutilisés, optimisant ainsi la taille du bundle et évitant des conflits de priorité CSS.
- Mise à jour de la librairie `cunningham-react` vers la version 4.2.0.
- Correction d'un problème d'événements `right-click` interceptés par les portails du menu contextuel.

### Autres changements
- Correction d'une faute de typographie ("Ok" remplacé par "OK") dans les locales.
- Correction d'une traduction française pour l'accès restreint.
- Correction de la couleur du placeholder et de l'icône dans le composant de recherche rapide.
- Correction d'un problème de re-rendu du composant `LaGaufreV2`.
- Correction de la responsivité du menu utilisateur.
- Ajout de l'export du composant `LaGaufreV2`.
