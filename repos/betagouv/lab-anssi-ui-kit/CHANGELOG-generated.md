## Changelog : lab-anssi-ui-kit (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives aux composants existants, notamment pour les champs de saisie (DsfrInput), les alertes (DsfrAlert), les listes déroulantes (DsfrDropdown) et les vignettes (DsfrTile). Des corrections de bugs et des améliorations de l'accessibilité ont également été apportées. La sécurité a été renforcée avec l'ajout d'outils d'analyse de code.

### Évolutions fonctionnelles
- Ajout de la possibilité de masquer le label du composant `DsfrToggle` grâce à la propriété `hideLabel`.
- Le composant `DsfrInput` propose désormais des variations 'addon' et 'action' pour associer un bouton submit ou d'action au champ de saisie.
- Ajout d'une propriété `noIcon` au composant `DsfrTile` pour masquer l'icône associée au lien.
- Amélioration de l'accessibilité du composant `DsfrDropdown` avec la possibilité de le désactiver via la prop `disabled`.
- Le composant `DsfrAlert` permet désormais de personnaliser la balise HTML du titre grâce à la propriété `titleTag`.
- Ajout de la prise en charge des couleurs hover et active pour le composant `DsfrTag` dans le thème MSC.
- Ajout de stories d'exemples pour le composant `DsfrInput` afin de couvrir l'ensemble des variations du DSFR.
- Amélioration de l'organisation des stories d'exemples pour une meilleure lisibilité.

### Évolutions techniques
- Mise à jour des dépendances : Svelte, Vite, Storybook, Vitest, PostCSS, Playwright, TypeScript, ESLint, etc.
- Renforcement de la sécurité : ajout des outils `checkov` et `zizmor` pour la validation de la configuration et correction des vulnérabilités potentielles.
- Sécurisation du workflow CI : désactivation des identifiants `git` des dépôts clonés et prévention des injections.
- Amélioration de la configuration du workflow CI pour utiliser la référence du dépôt et un fetch-depth de 0.
- Refactorisation du code du composant `DsfrInput` pour une meilleure maintenabilité.
- Optimisation du composant `DsfrSegmented` avec l'utilisation de `requestAnimationFrame` pour améliorer les performances lors du redimensionnement.
- Ajout de la configuration pour Code Connect (Figma).
- Ajout d'un fichier `renovate.json` pour la gestion automatisée des dépendances.

### Autres changements
- Documentation : Amélioration de la documentation et ajout de stories d'exemples.
- Version du kit mise à jour à la version 1.55.1.
- Uniformisation de la structure et du style du composant `PresentationANSSI` avec les éléments du DSFR.
- Correction de l'alignement à droite du menu déroulant du composant `DsfrDropdown`.
- Correction de l'affichage de l'état checked du composant `DsfrToggle`.
- Ajout de la gestion du style pour l'état disabled du composant `DsfrCheckbox`.
- Ajout d'une action pour gérer la propriété `--row-height` du composant `DsfrTable`.
- Ajout d'une story exemple de tableau avec lignes désactivées pour le composant `DsfrTable`.
- Ajout de la prise en charge de la taille et de la graisse pour les légendes des composants `DsfrCheckboxesGroup` et `DsfrRadiosGroup`.
- Ajout de la prise en charge de la taille et de la graisse pour le composant `DsfrLabel`.
- Remplacement de l'usage de la balise `label` par le composant `DsfrLabel`.
- Ajout du composant `DsfrLabel`.
