## Changelog : lab-anssi-ui-kit (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives aux composants DSFR, notamment pour les champs de saisie (DsfrInput) et les alertes (DsfrAlert), avec l'ajout de nouvelles fonctionnalités et variations. Des améliorations de sécurité ont également été intégrées au processus de CI/CD. Enfin, la configuration de l'outil Renovate a été mise à jour et de nouvelles stories d'exemple ont été ajoutées pour faciliter l'utilisation des composants.

### Évolutions fonctionnelles
- Ajout de la prop `hideLabel` au composant `DsfrToggle` pour masquer le label. [#issue_lien_si_disponible]
- Correction de l'alignement à droite du menu déroulant du composant `DsfrDropdown`. [#issue_lien_si_disponible]
- Ajout de la prop `titleTag` au composant `DsfrAlert` pour personnaliser la balise HTML du titre. [#issue_lien_si_disponible]
- Ajout de variations 'addon' et 'action' au composant `DsfrInput` pour associer des boutons au champ de saisie. [#issue_lien_si_disponible]
- Ajout de stories d'exemple pour le composant `DsfrInput` afin de couvrir l'ensemble des variations du DSFR. [#issue_lien_si_disponible]
- Ajout de la prise en charge de la taille et de la graisse pour les légendes des composants `DsfrCheckboxesGroup` et `DsfrRadiosGroup`. [#issue_lien_si_disponible]
- Ajout de la prise en charge de la taille et de la graisse pour le composant `DsfrLabel`. [#issue_lien_si_disponible]
- Remplacement de l'utilisation de la balise `label` par le composant `DsfrLabel` dans divers endroits. [#issue_lien_si_disponible]
- Ajout de la prop `disabled` au composant `DsfrDropdown` pour désactiver le bouton d'ouverture. [#issue_lien_si_disponible]
- Ajout de la configuration pour Code Connect dans Figma. [#issue_lien_si_disponible]
- Amélioration de l'organisation des stories d'exemples. [#issue_lien_si_disponible]

### Évolutions techniques
- Mise à jour des dépendances : Svelte, PostCSS, Playwright, Style Dictionary, ESLint, Testing Library, Vitest, Storybook, pnpm, typescript-eslint, globals, @types/node.
- Optimisation du composant `DsfrSegmented` avec `requestAnimationFrame` pour améliorer la réactivité. [#issue_lien_si_disponible]
- Ajout de `checkov` et `zizmor` pour valider la configuration de sécurité. [#issue_lien_si_disponible]
- Désactivation des identifiants `git` des dépôts clonés pour renforcer la sécurité. [#issue_lien_si_disponible]
- Éviter les injections dans le CI. [#issue_lien_si_disponible]
- Mise à jour de l'étape de checkout du CI pour utiliser la référence du dépôt et un fetch-depth de 0. [#issue_lien_si_disponible]
- Ajout et configuration de Renovate pour la gestion des dépendances. [#issue_lien_si_disponible]
- Uniformisation de la structure et du style du composant `PresentationANSSI` avec les éléments du DSFR. [#issue_lien_si_disponible]
- Ajout de couleurs hover et active pour le composant `DsfrTag` dans le thème MSC. [#issue_lien_si_disponible]

### Autres changements
- Passage à la version 1.55.1, 1.55.0 et 1.54.2.
- Mise à jour du formattage du fichier `renovate.json`.
- Épingle des versions des dépendances des GitHub Actions.
