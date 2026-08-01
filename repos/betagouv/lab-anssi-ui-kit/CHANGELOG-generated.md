## Changelog : lab-anssi-ui-kit (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la compatibilité des composants avec le Design System de la République Française (DSFR), notamment pour le carrousel, la marelle, les boutons et les modales. Des optimisations de performance ont été apportées au composant Segmented. La sécurité a été renforcée avec l'ajout d'outils d'analyse statique et des corrections concernant la gestion des identifiants Git dans les workflows CI/CD. Enfin, plusieurs mises à jour de dépendances ont été effectuées pour assurer la stabilité et la sécurité du projet.

### Évolutions fonctionnelles
- **DSFR :** Ajout du composant `DsfrTooltip`. [#9b9083a](https://github.com/betagouv/lab-anssi-ui-kit/commit/9b9083a)
- **CarrouselTuiles :** Rendu compatible avec le DSFR. [#9b9083a](https://github.com/betagouv/lab-anssi-ui-kit/commit/9b9083a)
- **Marelle :** Rendu compatible avec le DSFR. [#33caa4f](https://github.com/betagouv/lab-anssi-ui-kit/commit/33caa4f)
- **DsfrButton :** Ajout des variations inversées tertiaires et tertiaires sans bordure. [#9f339cc](https://github.com/betagouv/lab-anssi-ui-kit/commit/9f339cc)
- **DsfrModal :** Ajout du composant et implémentation du "trapFocus" pour une meilleure accessibilité. [#f69a522](https://github.com/betagouv/lab-anssi-ui-kit/commit/f69a522), [#7843bd1](https://github.com/betagouv/lab-anssi-ui-kit/commit/7843bd1), [#13f6453](https://github.com/betagouv/lab-anssi-ui-kit/commit/13f6453)
- **DsfrConnect :** Ajout de l'attribut `disabled` au lien du composant. [#f9bfa75](https://github.com/betagouv/lab-anssi-ui-kit/commit/f9bfa75)
- **DsfrTagsGroup :** Définition de la valeur par défaut de la prop `groupMarkup`. [#f32294a](https://github.com/betagouv/lab-anssi-ui-kit/commit/f32294a)
- **DsfrSegmented :** Optimisation de la gestion du `ResizeObserver` avec `requestAnimationFrame` pour améliorer la performance. [#4dab6e7](https://github.com/betagouv/lab-anssi-ui-kit/commit/4dab6e7)
- **Marelle :** Amélioration de la "slotabilité" des étapes. [#e8c5cf5](https://github.com/betagouv/lab-anssi-ui-kit/commit/e8c5cf5)
- **DsfrCallout :** Rendre le label du bouton optionnel. [#26fcda3](https://github.com/betagouv/lab-anssi-ui-kit/commit/26fcda3)
- **DsfrSelect :** Ajout de l'attribut `hide-label` à la story du composant. [#1f5fb9f](https://github.com/betagouv/lab-anssi-ui-kit/commit/1f5fb9f)

### Évolutions techniques
- **Sécurité CI/CD :** Ajout des outils `checkov` et `zizmor` pour l'analyse statique de la configuration et la détection de vulnérabilités. [#27897d5](https://github.com/betagouv/lab-anssi-ui-kit/commit/27897d5)
- **Sécurité CI/CD :** Correction de failles potentielles d'injection et désactivation des identifiants Git dans les workflows CI/CD. [#df25557](https://github.com/betagouv/lab-anssi-ui-kit/commit/df25557), [#c048ebc](https://github.com/betagouv/lab-anssi-ui-kit/commit/c048ebc)
- **Dépendances :** Mise à jour de plusieurs dépendances (Node.js, PNPM, Storybook, ESLint, TypeScript, Vitest, Playwright, style-dictionary, etc.) pour bénéficier des dernières corrections et améliorations.
- **Configuration :** Ajout de la configuration pour Code Connect (Figma). [#48ac321](https://github.com/betagouv/lab-anssi-ui-kit/commit/48ac321)
- **Renovate :** Mise à jour de la configuration Renovate pour améliorer la gestion des mises à jour de dépendances. [#c859428](https://github.com/betagouv/lab-anssi-ui-kit/commit/c859428)

### Autres changements
- **Storybook :** Réorganisation des titres des composants Lab ANSSI et DSFR, suppression des options de tri des stories. [#e177d4d](https://github.com/betagouv/lab-anssi-ui-kit/commit/e177d4d), [#cd06738](https://github.com/betagouv/lab-anssi-ui-kit/commit/cd06738), [#311dd6d](https://github.com/betagouv/lab-anssi-ui-kit/commit/311dd6d)
- **Version :** Passage à la version 1.57.0, 1.56.0, 1.55.2 et 1.55.1. [#bc59120](https://github.com/betagouv/lab-anssi-ui-kit/commit/bc59120), [#ee62cc8](https://github.com/betagouv/lab-anssi-ui-kit/commit/ee62cc8), [#104fad1](https://github.com/betagouv/lab-anssi-ui-kit/commit/104fad1), [#76da5b5](https://github.com/betagouv/lab-anssi-ui-kit/commit/76da5b5)
