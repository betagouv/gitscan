## Changelog : lab-anssi-ui-kit (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la bibliothèque, notamment l'ajout de nouveaux composants DSFR (Modal, Label) et des améliorations à l'accessibilité (trapFocus sur le modal). Des optimisations de performance ont été apportées au composant DsfrSegmented. La sécurité a également été renforcée avec l'ajout d'outils d'analyse de code et la correction de vulnérabilités potentielles dans le CI/CD.

### Évolutions fonctionnelles
- Ajout du composant `DsfrModal` avec gestion du focus (trapFocus) [#7843bd1](https://github.com/betagouv/lab-anssi-ui-kit/issues/7843bd1)
- Ajout du composant `DsfrLabel` pour une meilleure sémantique et accessibilité. [#9a1cd34](https://github.com/betagouv/lab-anssi-ui-kit/issues/9a1cd34)
- Amélioration du composant `DsfrSegmented` avec une optimisation de `ResizeObserver` pour de meilleures performances. [#4dab6e7](https://github.com/betagouv/lab-anssi-ui-kit/issues/4dab6e7)
- Le composant `DsfrConnect` permet maintenant de désactiver le lien. [#f9bfa75](https://github.com/betagouv/lab-anssi-ui-kit/issues/f9bfa75)
- Le composant `DsfrCallout` permet maintenant de rendre le label du bouton optionnel. [#26fcda3](https://github.com/betagouv/lab-anssi-ui-kit/issues/26fcda3)
- Ajout de l'attribut `hide-label` à la story du composant `DsfrSelect`. [#1f5fb9f](https://github.com/betagouv/lab-anssi-ui-kit/issues/1f5fb9f)
- Amélioration de la flexibilité des étapes du composant `Marello` grâce à l'ajout de slots. [#e8c5cf5](https://github.com/betagouv/lab-anssi-ui-kit/issues/e8c5cf5)
- Prise en charge de la taille et de la graisse pour les légendes des composants `DsfrCheckboxesGroup` et `DsfrRadiosGroup`. [#7e37811](https://github.com/betagouv/lab-anssi-ui-kit/issues/7e37811)
- Remplacement de l'utilisation de la balise `<label>` par le composant `DsfrLabel` dans divers composants. [#4e3c862](https://github.com/betagouv/lab-anssi-ui-kit/issues/4e3c862)

### Évolutions techniques
- Mise à jour de PNPM vers la version 11.17.0 pour des raisons de sécurité. [#937e764](https://github.com/betagouv/lab-anssi-ui-kit/issues/937e764)
- Fixation de la version de Node.js à la dernière version LTS (24.18.0) pour garantir la stabilité. [#2928487](https://github.com/betagouv/lab-anssi-ui-kit/issues/2928487)
- Mise à jour de Storybook vers la version 10.5.0. [#e9d11c9](https://github.com/betagouv/lab-anssi-ui-kit/issues/e9d11c9)
- Ajout de Renovate pour la gestion automatisée des dépendances et la configuration des commits. [#c859428](https://github.com/betagouv/lab-anssi-ui-kit/issues/c859428) et [#df0ebdc](https://github.com/betagouv/lab-anssi-ui-kit/issues/df0ebdc)
- Ajout d'outils d'analyse de sécurité au CI/CD : `checkov` et `zizmor`. [#27897d5](https://github.com/betagouv/lab-anssi-ui-kit/issues/27897d5)
- Correction de vulnérabilités potentielles dans le CI/CD en désactivant les identifiants `git` des dépôts clonés. [#c048ebc](https://github.com/betagouv/lab-anssi-ui-kit/issues/c048ebc)
- Ajout de la configuration pour Code Connect (Figma). [#48ac321](https://github.com/betagouv/lab-anssi-ui-kit/issues/48ac321)

### Autres changements
- Réorganisation des titres des composants Lab ANSSI et DSFR dans Storybook. [#e177d4d](https://github.com/betagouv/lab-anssi-ui-kit/issues/e177d4d) et [#311dd6d](https://github.com/betagouv/lab-anssi-ui-kit/issues/311dd6d)
- Suppression des options de tri des stories dans Storybook. [#cd06738](https://github.com/betagouv/lab-anssi-ui-kit/issues/cd06738)
- Passage à la version 1.56.0 puis 1.55.2 et 1.55.1 et 1.55.0. [#ee62cc8](https://github.com/betagouv/lab-anssi-ui-kit/issues/ee62cc8), [#76da5b5](https://github.com/betagouv/lab-anssi-ui-kit/issues/76da5b5), [#104fad1](https://github.com/betagouv/lab-anssi-ui-kit/issues/104fad1) et [#6bb244f](https://github.com/betagouv/lab-anssi-ui-kit/issues/6bb244f)
