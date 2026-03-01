## Changelog : ui-kit (30 derniers jours)

### Résumé
Les dernières mises à jour du kit d'interface utilisateur se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du partage de données, du menu utilisateur et de l'onboarding. Des corrections de bugs et des améliorations de la documentation ont également été apportées. Plusieurs mises à jour de composants et de dépendances ont été intégrées pour une meilleure performance et stabilité.

### Évolutions fonctionnelles
- Correction du padding du menu utilisateur [#175](https://github.com/suitenumerique/ui-kit/issues/175).
- Amélioration de la visibilité de l'option de suppression dans le menu des rôles d'accès.
- Ajout d'une propriété `can_delete` au type `AccessData` pour contrôler la visibilité de l'option de suppression.
- Ajout du composant `ReleaseNoteModal` pour afficher les notes de version.
- Amélioration du composant `OnboardingModal` avec un mode texte uniquement et une animation de description.
- Correction de l'affichage de l'option de suppression dans le menu déroulant des rôles d'accès.
- Correction d'une faute de frappe ("Ok" remplacé par "OK") dans les traductions.
- Correction du lien dans le pied de page du modal d'onboarding et amélioration du style.
- Correction du type `apiUrl` dans le composant `LaGaufreV2`.
- Amélioration de la documentation du composant `ShareModal` dans Storybook.

### Évolutions techniques
- Mise à jour de la dépendance `cunningham-react` vers la version 4.2.0.
- Suppression d'imports de styles inutilisés de `cunningham-react`.
- Refactoring du code pour déplacer l'action de suppression dans le composant `AccessRoleDropdown`.
- Utilisation de composants d'icônes React en ligne au lieu d'images SVG pour le partage.
- Utilisation du composant `Button` de Cunningham pour le menu d'accès au rôle.
- Correction d'un problème d'événements de clic droit sur les portails du menu contextuel.

### Autres changements
- Ajout de documentation complète au fichier README.
- Ajout de stories pour la fonctionnalité `can_delete`.
- Amélioration de la documentation des stories pour le composant `OnboardingModal`.
- Correction de la couleur du placeholder et de l'icône dans le champ de recherche rapide.
- Ajout de documentation sur l'utilisation du composant `ReleaseNoteModal`.
- Ajout de stories pour la fonctionnalité `can_delete`.
