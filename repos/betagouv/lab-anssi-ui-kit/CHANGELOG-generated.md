## Changelog : lab-anssi-ui-kit (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à plusieurs composants, notamment `DsfrDropdown`, `DsfrToggle`, `DsfrInput` et `DsfrAlert`, en ajoutant de nouvelles fonctionnalités et en corrigeant des problèmes d'affichage. Des efforts ont également été faits pour améliorer la sécurité du processus de CI/CD et la documentation. Enfin, plusieurs composants ont été mis à jour pour mieux respecter les standards du DSFR.

### Évolutions fonctionnelles
- Ajout de la possibilité de désactiver le bouton d'ouverture du composant `DsfrDropdown` via la prop `disabled`.
- Le composant `DsfrToggle` permet désormais de masquer le label grâce à la propriété `hideLabel`.
- Correction de l'affichage de l'état "checked" du composant `DsfrToggle`.
- Le composant `DsfrInput` gagne de nouvelles variations : `addon` (avec un bouton submit) et `action` (avec un bouton d'action).
- Ajout de la prop `titleTag` au composant `DsfrAlert` pour personnaliser la balise HTML du titre.
- Amélioration de l'affichage du titre et de la description du composant `DsfrAlert` en fonction de la taille.
- Ajout de la prise en charge des couleurs hover et active pour le composant `DsfrTag` dans le thème MSC.
- Le composant `PresentationANSSI` a été uniformisé avec les éléments du DSFR.
- Ajout de la possibilité de rendre les étapes du composant `Marellette` plus "slotable".
- Ajout de la prise en charge de la taille et de la graisse pour les légendes des composants `DsfrCheckboxesGroup` et `DsfrRadiosGroup`.
- Ajout de la prise en charge de la taille et de la graisse pour le composant `DsfrLabel`.
- Remplacement de l'utilisation de la balise `<label>` par le composant `DsfrLabel` dans plusieurs endroits.
- Ajout du composant `DsfrLabel`.

### Évolutions techniques
- Mise à jour des dépendances : Svelte, SvelteKit, TypeScript, ESLint, Vitest, Storybook, PostCSS, Playwright, style-dictionary, etc.
- Optimisation du composant `DsfrSegmented` avec l'utilisation de `requestAnimationFrame` pour améliorer les performances lors du redimensionnement.
- Ajout de `checkov` et `zizmor` pour valider la configuration de sécurité.
- Sécurisation du CI/CD : désactivation des identifiants `git` des dépôts clonés et prévention des injections.
- Amélioration de la configuration du checkout dans le CI pour utiliser la référence du dépôt et un fetch-depth de 0.
- Ajout d'un fichier `renovate.json` pour la gestion automatisée des dépendances.
- Refactoring du code du composant `DsfrInput`.
- Ajout de la configuration pour Code Connect dans Figma.

### Autres changements
- Amélioration de l'organisation des stories d'exemples dans la documentation.
- Passage à la version 1.55.2, 1.55.1, 1.55.0 et 1.54.2.
- Correction de l'alignement à droite du menu déroulant du composant `DsfrDropdown`.
