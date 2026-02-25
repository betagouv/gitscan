## Changelog : ui-kit (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à la bibliothèque de composants, notamment l'ajout de nouveaux composants comme le menu contextuel et le modal d'onboarding, ainsi que des corrections de bugs et des améliorations de l'expérience utilisateur sur des composants existants comme le menu de partage et la recherche rapide. Des mises à jour de dépendances et de documentation ont également été réalisées.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant `ReleaseNoteModal` pour afficher les notes de version.
- Ajout d'un nouveau composant `OnboardingModal` avec un mode texte uniquement et une animation de description (#175).
- Amélioration du composant `ShareModal` avec la possibilité de masquer l'option de suppression en fonction d'un booléen `canDelete`.
- Ajout de séparateurs et d'une variante "danger" au composant `DropdownMenu`.
- Ajout d'un menu contextuel accessible (`ContextMenu`) avec des callbacks `onFocus` et `onBlur` pour le suivi des interactions.
- Correction de l'affichage de l'option de suppression dans le menu déroulant des rôles d'accès.
- Correction du padding du menu utilisateur.
- Correction de la couleur du placeholder et de l'icône dans la recherche rapide.
- Correction d'un bug dans `LaGaufreV2` concernant le type `apiUrl`.

### Évolutions techniques
- Mise à jour de la dépendance `cunningham-react` vers la version 4.2.0.
- Suppression des importations de styles inutilisées de `cunningham-react`.
- Refactoring du code pour déplacer l'action de suppression dans le composant `AccessRoleDropdown`.
- Ajout d'un type `MenuItem` partagé pour les composants `ContextMenu` et `DropdownMenu`.
- Suppression du répertoire `openspec` du suivi Git.

### Autres changements
- Amélioration de la documentation du composant `ShareModal` dans Storybook.
- Ajout de documentation complète au fichier README.
- Ajout de stories pour la fonctionnalité `can_delete` du composant `ShareModal`.
- Correction d'une faute de frappe ("Ok" -> "OK") dans les locales.
- Correction d'une traduction française restreinte.
- Ajout de documentation d'utilisation pour les composants `DropdownMenu` et `OnboardingModal`.
- Ajout de specs pour le menu contextuel avec le type `MenuItem` unifié.
