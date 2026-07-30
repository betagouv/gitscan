## Changelog : lab-anssi-ui-kit (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la compatibilité avec le Design System Français (DSFR), avec l'ajout de nouveaux composants (DsfrTooltip, DsfrModal) et l'amélioration de composants existants (DsfrButton, DsfrConnect, DsfrSegmented, DsfrTabnav, DsfrRange, DsfrCheckboxesGroup, DsfrRadiosGroup). Des optimisations de sécurité ont également été implémentées dans le processus de CI/CD.

### Évolutions fonctionnelles
- Ajout du composant `DsfrTooltip` pour afficher des infobulles d'aide.
- Ajout du composant `DsfrModal` pour afficher des boîtes de dialogue modales, avec implémentation du "trapFocus" pour une meilleure accessibilité.
- Le composant `DsfrButton` bénéficie de nouvelles variations : inversé tertiaire et tertiaire sans bordure.
- Le composant `LabCarrouselTuiles` est maintenant compatible avec le DSFR.
- Le composant `LabMarelle` est maintenant compatible avec le DSFR.
- Amélioration du composant `DsfrConnect` avec l'ajout d'un attribut `disabled` au lien.
- Amélioration du composant `DsfrSegmented` avec une optimisation du `ResizeObserver` utilisant `requestAnimationFrame`.
- Amélioration du composant `DsfrTabnav` avec la prise en charge de `createSlot` pour les liens.
- Amélioration des composants `DsfrCheckboxesGroup` et `DsfrRadiosGroup` avec la prise en charge de la taille et de la graisse des légendes.
- Amélioration du composant `DsfrLabel` avec la prise en charge de la taille et de la graisse.
- Remplacement de l'utilisation de la balise `label` par le composant `DsfrLabel` dans plusieurs composants.
- Ajout de la possibilité de masquer le label du composant `DsfrSelect`.

### Évolutions techniques
- Mise à jour de PNPM vers la version 11.17.0 pour des raisons de sécurité.
- Fixe de la version de Node.js à la dernière version LTS (24.18.0) pour assurer la stabilité.
- Mise à jour de Storybook vers la version 10.5.0.
- Amélioration de la configuration de Renovate pour une meilleure gestion des dépendances et des commits.
- Ajout de configurations pour Code Connect (Figma).
- Ajout de `checkov` et `zizmor` pour la validation de la configuration de sécurité.
- Désactivation des identifiants `git` des dépôts clonés pour renforcer la sécurité du CI.
- Éviter les injections dans le CI.

### Autres changements
- Réorganisation des titres des composants Lab ANSSI et DSFR dans Storybook.
- Suppression des options de tri des stories dans Storybook.
- Ajout de boutons inversés aux stories du composant `LabAnssiBandeauPage`.
- Ajout d'un fichier `renovate.json` pour la configuration de Renovate.
- Mise à jour de diverses dépendances (eslint, vitest, playwright, style-dictionary, etc.).
