## Changelog : lab-anssi-ui-kit (30 derniers jours, au 20 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la bibliothèque, notamment l'ajout de nouveaux composants comme le "Bandeau page" et des variations pour la navigation (Mega Menu) et les tableaux (sélectionnable).  De plus, la validation des formulaires a été implémentée pour plusieurs composants, améliorant l'expérience utilisateur et la conformité aux standards web.  Des améliorations de la thématisation et de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout du composant "Bandeau page" [#c79a246](https://github.com/betagouv/lab-anssi-ui-kit/pulls/c79a246).
- Ajout de la variation "Mega Menu" au composant `DsfrNavigation` [#2fef22e](https://github.com/betagouv/lab-anssi-ui-kit/pulls/2fef22e).
- Ajout de la possibilité d'insérer des slots dans les 'Mega Menus' du composant `DsfrNavigation` [#2e0b522](https://github.com/betagouv/lab-anssi-ui-kit/pulls/2e0b522).
- Ajout de la variation 'selectable' au composant `DsfrTable` [#61aec1b](https://github.com/betagouv/lab-anssi-ui-kit/pulls/61aec1b).
- Ajout de la fonctionnalité 'tout sélectionner' pour la sélection des lignes dans le composant `DsfrTable` [#21a3221](https://github.com/betagouv/lab-anssi-ui-kit/pulls/21a3221).
- Ajout de la variation 'indeterminate' au composant `DsfrCheckbox` [#5dcbb87](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5dcbb87).
- Ajout du composant `DsfrMessagesGroup` [#841278f](https://github.com/betagouv/lab-anssi-ui-kit/pulls/841278f).
- Ajout du composant `DsfrUser` [#d356018](https://github.com/betagouv/lab-anssi-ui-kit/pulls/d356018).
- Ajout d'un slot pour une image personnalisée dans le composant `DsfrCard` [#0dad2f1](https://github.com/betagouv/lab-anssi-ui-kit/pulls/0dad2f1).
- Ajout d'un slot pour un bouton dans le composant `DsfrNavigation` [#a091cc6](https://github.com/betagouv/lab-anssi-ui-kit/pulls/a091cc6).
- Ajout d'un slot pour le contenu du Header MSS (connecté) [#4d04a65](https://github.com/betagouv/lab-anssi-ui-kit/pulls/4d04a65).

### Évolutions techniques
- Uniformisation des variations personnalisées des `DsfrButton` et `DsfrButtonsGroup` [#ad7c9e9](https://github.com/betagouv/lab-anssi-ui-kit/pulls/ad7c9e9).
- Ajout de la propriété 'lab-border-radius' comme thématisable [#014010f](https://github.com/betagouv/lab-anssi-ui-kit/pulls/014010f).
- Implémentation de la validation des contraintes HTML pour les composants `DsfrCheckbox`, `DsfrCheckboxesGroup`, `DsfrInput`, `DsfrTextarea` et `DsfrSelect` [#f916fb4](https://github.com/betagouv/lab-anssi-ui-kit/pulls/f916fb4), [#b16e557](https://github.com/betagouv/lab-anssi-ui-kit/pulls/b16e557), [#a098657](https://github.com/betagouv/lab-anssi-ui-kit/pulls/a098657), [#9e5eac1](https://github.com/betagouv/lab-anssi-ui-kit/pulls/9e5eac1), [#5727e92](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5727e92).
- Refactoring du code et suppression de fonctionnalités inutilisées dans le composant `DsfrTable` [#ff4afa7](https://github.com/betagouv/lab-anssi-ui-kit/pulls/ff4afa7).
- Suppression de l'implémentation de la fonctionnalité 'render' propre aux usages Svelte dans le composant `DsfrTable` [#b5349fa](https://github.com/betagouv/lab-anssi-ui-kit/pulls/b5349fa).
- Ajout de CustomEvent pour les changements de page et de lignes par page dans le composant `DsfrTable` [#8588078](https://github.com/betagouv/lab-anssi-ui-kit/pulls/8588078).
- Renommage des événements du composant `DsfrTable` pour plus de cohérence [#6fe796e](https://github.com/betagouv/lab-anssi-ui-kit/pulls/6fe796e).
- Mise à jour des dépendances obsolètes [#87cd2be](https://github.com/betagouv/lab-anssi-ui-kit/pulls/87cd2be).
- Modification de la structure de `MenuItem` du composant `DsfrNavigation` [#63073f3](https://github.com/betagouv/lab-anssi-ui-kit/pulls/63073f3).
- Ajout d'un paramètre pour activer ou désactiver le thème [#f38464f](https://github.com/betagouv/lab-anssi-ui-kit/pulls/f38464f).
- Spécification de l'usage du sélecteur `[data-themeable]` pour l'application des thèmes [#d7a04b2](https://github.com/betagouv/lab-anssi-ui-kit/pulls/d7a04b2).
- Ajout de la définition des couleurs pour les éléments non thématisables [#5a6b775](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5a6b775).
- Définition explicite des composants `Header` et `Footer` comme non thématisables [#463d434](https://github.com/betagouv/lab-anssi-ui-kit/pulls/463d434).
- Associe les custom elements aux formulaires web natifs [#1309779](https://github.com/betagouv/lab-anssi-ui-kit/pulls/1309779).

### Autres changements
- Amélioration de la documentation et des stories du composant `DsfrNavigation` [#2e0b522](https://github.com/betagouv/lab-anssi-ui-kit/pulls/2e0b522).
- Amélioration de la documentation du composant `DsfrTable` et des stories associées [#5dca978](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5dca978).
- Ajout d'une section expliquant comment désactiver la thématisation d'un composant [#7a735ac](https://github.com/betagouv/lab-anssi-ui-kit/pulls/7a735ac).
- Organisation des exemples pour la carte de jeu dans Storybook [#a461fe6](https://github.com/betagouv/lab-anssi-ui-kit/pulls/a461fe6).
- Ajout d'un exemple de `DsfrTabs` avec un système de notifications dans Storybook [#8cb3656](https://github.com/betagouv/lab-anssi-ui-kit/pulls/8cb3656).
- Suppression de l'exemple de LandingMAC dans Storybook [#866dc4b](https://github.com/betagouv/lab-anssi-ui-kit/pulls/866dc4b).
- Amélioration de la story du Header et ajout de nouvelles stories dans Storybook [#472fe20](https://github.com/betagouv/lab-anssi-ui-kit/pulls/472fe20).
- Ajout d'un exemple d'un `DsfrButton` avec un indicateur de notification dans Storybook [#472fe20](https://github.com/betagouv/lab-anssi-ui-kit/pulls/472fe20).
- Correction du style pour les cases à cocher 'checked' et 'indeterminate' dans le composant `DsfrCheckbox` [#0212aca](https://github.com/betagouv/lab-anssi-ui-kit/pulls/0212aca).
- Correction de l'affichage du caption dans le composant `DsfrTable` [#96dc229](https://github.com/betagouv/lab-anssi-ui-kit/pulls/96dc229).
- Correction des breakpoints de la `NavigationSuiteCyber` [#7b24ea6](https://github.com/betagouv/lab-anssi-ui-kit/pulls/7b24ea6).
- Correction de l'affichage du statut "actif" des sous-items de la navigation [#98de9f2](https://github.com/betagouv/lab-anssi-ui-kit/pulls/98de9f2).
- Correction de l'application du `disabled` sur les input du composant `DsfrRadiosGroup` [#6b6d98a](https://github.com/betagouv/lab-anssi-ui-kit/pulls/6b6d98a).
- Modification du wording du bouton Diagnostic [#57cccc2](https://github.com/betagouv/lab-anssi-ui-kit/pulls/57cccc2).
- Remplacement des citations LAB par les citations DSFR [#7b24ea6](https://github.com/betagouv/lab-anssi-ui-kit/pulls/7b24ea6).
- Ajout de styles de fallback pour le conteneur dsfr [#29fecba](https://github.com/betagouv/lab-anssi-ui-kit/pulls/29fecba).
- Rend l'attribut `contentDescription` optionnel dans le Footer [#6d3d2f0](https://github.com/betagouv/lab-anssi-ui-kit/pulls/6d3d2f0).
