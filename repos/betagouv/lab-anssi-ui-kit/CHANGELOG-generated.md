## Changelog : lab-anssi-ui-kit (30 derniers jours, au 2026-05-15)

### Résumé
Ce mois-ci, le UI Kit a connu des améliorations significatives sur le composant Table, avec l'ajout de fonctionnalités de sélection et de pagination, ainsi que des corrections de style et de documentation. Des améliorations ont également été apportées aux composants Header, Navigation, Checkbox et Card, ainsi qu'une implémentation de la validation HTML pour plusieurs formulaires. La thématisation a été revue et des corrections ont été apportées à la NavigationSuiteCyber.

### Évolutions fonctionnelles
- Ajout de la variation 'selectable' au composant `DsfrTable` [#61aec1b](https://github.com/betagouv/lab-anssi-ui-kit/commit/61aec1b).
- Implémentation de la fonctionnalité 'tout sélectionner' pour la sélection des lignes dans `DsfrTable` [#21a3221](https://github.com/betagouv/lab-anssi-ui-kit/commit/21a3221).
- Ajout de la variation 'indeterminate' au composant `DsfrCheckbox` [#5dcbb87](https://github.com/betagouv/lab-anssi-ui-kit/commit/5dcbb87).
- Ajout du type de bouton et amélioration de la gestion des événements de soumission pour le composant `DsfrSearch` [#c769700](https://github.com/betagouv/lab-anssi-ui-kit/commit/c769700).
- Ajout d'un slot pour insérer une image personnalisée dans le composant `DsfrCard` [#9911bac](https://github.com/betagouv/lab-anssi-ui-kit/commit/9911bac).
- Ajout du composant `DsfrUser` [#d356018](https://github.com/betagouv/lab-anssi-ui-kit/commit/d356018).
- Ajout du composant `DsfrMessagesGroup` [#841278f](https://github.com/betagouv/lab-anssi-ui-kit/commit/841278f).
- Possibilité d'ajouter un bouton à la `DsfrNavigation` [#298d052](https://github.com/betagouv/lab-anssi-ui-kit/commit/298d052).
- Ajout d'un slot pour le Header MSS (connecté et non connecté) [#feb4328](https://github.com/betagouv/lab-anssi-ui-kit/commit/feb4328) et [#c239ce7](https://github.com/betagouv/lab-anssi-ui-kit/commit/c239ce7).
- Implémentation de la validation des contraintes HTML pour les composants `DsfrCheckbox`, `DsfrCheckboxesGroup`, `DsfrInput`, `DsfrTextarea`, `DsfrSelect` et `DsfrSearch` [#f916fb4](https://github.com/betagouv/lab-anssi-ui-kit/commit/f916fb4), [#b16e557](https://github.com/betagouv/lab-anssi-ui-kit/commit/b16e557), [#a098657](https://github.com/betagouv/lab-anssi-ui-kit/commit/a098657), [#9e5eac1](https://github.com/betagouv/lab-anssi-ui-kit/commit/9e5eac1), [#5727e92](https://github.com/betagouv/lab-anssi-ui-kit/commit/5727e92), [#43164a5](https://github.com/betagouv/lab-anssi-ui-kit/commit/43164a5).

### Évolutions techniques
- Refactoring du composant `DsfrTable` : nettoyage du code, suppression de fonctionnalités inutilisées et retrait de l'implémentation Svelte spécifique [#ff4afa7](https://github.com/betagouv/lab-anssi-ui-kit/commit/ff4afa7), [#b5349fa](https://github.com/betagouv/lab-anssi-ui-kit/commit/b5349fa).
- Amélioration de la gestion des sous-menus dans le composant `DsfrNavigation` [#d8f8d5b](https://github.com/betagouv/lab-anssi-ui-kit/commit/d8f8d5b).
- Modification de la structure de `MenuItem` dans le composant `DsfrNavigation` [#63073f3](https://github.com/betagouv/lab-anssi-ui-kit/commit/63073f3).
- Ajout d'un paramètre pour activer ou désactiver le thème (thématisation) [#f38464f](https://github.com/betagouv/lab-anssi-ui-kit/commit/f38464f).
- Spécification de l'usage du sélecteur `[data-themeable]` pour l'application des thèmes [#d7a04b2](https://github.com/betagouv/lab-anssi-ui-kit/commit/d7a04b2).
- Extraction de la logique de validation dans une fonction externe pour une meilleure réutilisabilité [#9b0af34](https://github.com/betagouv/lab-anssi-ui-kit/commit/9b0af34).
- Association des custom elements aux formulaires web natifs [#1309779](https://github.com/betagouv/lab-anssi-ui-kit/commit/1309779).

### Autres changements
- Amélioration de la documentation du composant `DsfrTable` et des stories associées [#5dca978](https://github.com/betagouv/lab-anssi-ui-kit/commit/5dca978).
- Ajout de CustomEvent pour les changements de page et de lignes par page dans `DsfrTable` [#8588078](https://github.com/betagouv/lab-anssi-ui-kit/commit/8588078).
- Renommage des noms d'événements dans `DsfrTable` pour plus de cohérence [#6fe796e](https://github.com/betagouv/lab-anssi-ui-kit/commit/6fe796e).
- Ajout de la possibilité de passer une prop 'rich' par colonne dans `DsfrTable` [#54f571b](https://github.com/betagouv/lab-anssi-ui-kit/commit/54f571b).
- Organisation des exemples pour la carte de jeu dans Storybook [#a461fe6](https://github.com/betagouv/lab-anssi-ui-kit/commit/a461fe6).
- Ajout d'un exemple de `DsfrTabs` avec un système de notifications dans Storybook [#8cb3656](https://github.com/betagouv/lab-anssi-ui-kit/commit/8cb3656).
- Suppression de l'exemple de LandingMAC dans Storybook [#866dc4b](https://github.com/betagouv/lab-anssi-ui-kit/commit/866dc4b).
- Amélioration de la story du Header et ajout de nouvelles stories dans Storybook [#4d4bcb5](https://github.com/betagouv/lab-anssi-ui-kit/commit/4d4bcb5).
- Ajout d'un exemple d'un `DsfrButton` avec un indicateur de notification dans Storybook [#472fe20](https://github.com/betagouv/lab-anssi-ui-kit/commit/472fe20).
- Correction de l'application du `disabled` sur les inputs dans `DsfrRadiosGroup` [#6b6d98a](https://github.com/betagouv/lab-anssi-ui-kit/commit/6b6d98a).
- Correction des breakpoints de la `NavigationSuiteCyber` [#a091cc6](https://github.com/betagouv/lab-anssi-ui-kit/commit/a091cc6).
- Affichage du statut "actif" des sous-items de la navigation [#98de9f2](https://github.com/betagouv/lab-anssi-ui-kit/commit/98de9f2).
- Modification du wording du bouton diagnostic [#57cccc2](https://github.com/betagouv/lab-anssi-ui-kit/commit/57cccc2).
- Correction du type de l'attribut 'alt' et ajustement des valeurs par défaut dans `DsfrCard` [#26e2d22](https://github.com/betagouv/lab-anssi-ui-kit/commit/26e2d22).
- Ajout de styles de fallback pour le conteneur dsfr [#29fecba](https://github.com/betagouv/lab-anssi-ui-kit/commit/29fecba).
- Rendre la prop 'label' du bouton optionnel [#fe708d7](https://github.com/betagouv/lab-anssi-ui-kit/commit/fe708d7).
- Correction de l'affichage du caption dans `DsfrTable` [#96dc229](https://github.com/betagouv/lab-anssi-ui-kit/commit/96dc229).
- Rendre l'attribut `contentDescription` optionnel dans le Footer [#6d3d2f0](https://github.com/betagouv/lab-anssi-ui-kit/commit/6d3d2f0).
