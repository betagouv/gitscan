## Changelog : lab-anssi-ui-kit (30 derniers jours, au 21 avril 2026)

### Résumé
Cette version apporte de nombreuses améliorations et corrections, notamment autour des composants DSFR (Design System France). De nouveaux composants ont été ajoutés (User, Tabs, Tabnav, Notice) et des fonctionnalités ont été ajoutées aux composants existants (Header, Link, Checkbox, Segmented, etc.). Des corrections de sécurité ont également été appliquées et les dépendances ont été mises à jour.

### Évolutions fonctionnelles
- Ajout du composant `User` DSFR [#d356018](https://github.com/betagouv/lab-anssi-ui-kit/pulls/d356018).
- Ajout des composants `Tabs` et `Tabnav` DSFR [#83edacb](https://github.com/betagouv/lab-anssi-ui-kit/pulls/83edacb) et [#198cfa8](https://github.com/betagouv/lab-anssi-ui-kit/pulls/198cfa8).
- Ajout du composant `Notice` DSFR [#81b185f](https://github.com/betagouv/lab-anssi-ui-kit/pulls/81b185f).
- Ajout d'exemples de composants `Header` pour MQC et MSS [#c239ce7](https://github.com/betagouv/lab-anssi-ui-kit/pulls/c239ce7).
- Ajout d'une story d'exemple pour le `Header MSS` (connecté et non connecté) [#4d04a65](https://github.com/betagouv/lab-anssi-ui-kit/pulls/4d04a65) et [#feb4328](https://github.com/betagouv/lab-anssi-ui-kit/pulls/feb4328).
- Ajout d'un slot 'hint' au composant `DsfrCheckbox` [#633d112](https://github.com/betagouv/lab-anssi-ui-kit/pulls/633d112).
- Ajout d'un slot 'description' au composant `DsfrFooter` [#05a842b](https://github.com/betagouv/lab-anssi-ui-kit/pulls/05a842b).
- Ajout de la prop 'neutral' au composant `DsfrLink` [#c7d38ae](https://github.com/betagouv/lab-anssi-ui-kit/pulls/c7d38ae).
- Ajout de la prop 'hideDetails' au composant `DsfrStepper` [#590ce7e](https://github.com/betagouv/lab-anssi-ui-kit/pulls/590ce7e).
- Amélioration de la gestion du layout responsive du composant `DsfrSegmented` [#670fd88](https://github.com/betagouv/lab-anssi-ui-kit/pulls/670fd88).
- Ajout de slots pour personnaliser la barre de navigation et les liens d'outils du composant `DsfrHeader` [#6958024](https://github.com/betagouv/lab-anssi-ui-kit/pulls/6958024).
- Ajout de la propriété 'fluid' pour un conteneur fluide au composant `DsfrHeader` [#4630979](https://github.com/betagouv/lab-anssi-ui-kit/pulls/4630979).

### Évolutions techniques
- Mise à jour des dépendances : Svelte (5.55.0), TypeScript (6.0.2), Storybook (10.3.3), Vitest (4.1.1), DSFR (1.14.4) [#6b96626](https://github.com/betagouv/lab-anssi-ui-kit/pulls/6b96626), [#880b624](https://github.com/betagouv/lab-anssi-ui-kit/pulls/880b624), [#654d7b0](https://github.com/betagouv/lab-anssi-ui-kit/pulls/654d7b0), [#5ba71b2](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5ba71b2), [#15f4801](https://github.com/betagouv/lab-anssi-ui-kit/pulls/15f4801).
- Refactorisation des composants pour utiliser la fonction `withIconsStyleSheet` [#1f03fb4](https://github.com/betagouv/lab-anssi-ui-kit/pulls/1f03fb4).
- Utilisation de l'import SCSS à la place de l'import CSS dans `DsfrLink` [#5a22049](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5a22049).
- Application des patchs de sécurité suite aux alertes dependabot [#c63aaef](https://github.com/betagouv/lab-anssi-ui-kit/pulls/c63aaef) et [#d88cbe1](https://github.com/betagouv/lab-anssi-ui-kit/pulls/d88cbe1).
- Application d'un patch de sécurité concernant 'follow-redirects' [#5ff3d76](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5ff3d76).

### Autres changements
- Correction des breakpoints de la `NavigationSuiteCyber` [#a091cc6](https://github.com/betagouv/lab-anssi-ui-kit/pulls/a091cc6).
- Affichage du statut "actif" des sous-items de la navigation [#98de9f2](https://github.com/betagouv/lab-anssi-ui-kit/pulls/98de9f2).
- Correction du type de l'attribut 'alt' et ajustement des valeurs par défaut dans `DsfrCard` [#26e2d22](https://github.com/betagouv/lab-anssi-ui-kit/pulls/26e2d22).
- Ajout du type et du statut aux badges dans `DsfrBadgesGroup` [#fd0f385](https://github.com/betagouv/lab-anssi-ui-kit/pulls/fd0f385).
- Correction du passage de la prop 'inline' au composant `DsfrButtonsGroup` [#f7833b1](https://github.com/betagouv/lab-anssi-ui-kit/pulls/f7833b1).
- Rendre la prop 'label' du bouton optionnel dans `DsfrButton` [#fe708d7](https://github.com/betagouv/lab-anssi-ui-kit/pulls/fe708d7).
- Ajout d'une condition à l'affichage du service de marque dans `DsfrHeader` [#4a155e9](https://github.com/betagouv/lab-anssi-ui-kit/pulls/4a155e9).
- Amélioration du mode de calcul de la hauteur des onglets dans `DsfrTabs` [#8f64c67](https://github.com/betagouv/lab-anssi-ui-kit/pulls/8f64c67).
- Amélioration de la lisibilité des descriptions des slots dans les stories [#b53a03e](https://github.com/betagouv/lab-anssi-ui-kit/pulls/b53a03e).
- Ajout des descriptions des slots dans les stories [#7087728](https://github.com/betagouv/lab-anssi-ui-kit/pulls/7087728).
- Mise à jour des appels à la mixin `set-shadow-host` [#59841a8](https://github.com/betagouv/lab-anssi-ui-kit/pulls/59841a8).
- Modification du passage des tools links en JSON dans `DsfrHeader` [#5f87a35](https://github.com/betagouv/lab-anssi-ui-kit/pulls/5f87a35).
- Ajout de l'attribut 'id' pour le tag dans `DsfrTag` [#0ead556](https://github.com/betagouv/lab-anssi-ui-kit/pulls/0ead556).
- Revert de la publication non 'latest' sur npm [#f022064](https://github.com/betagouv/lab-anssi-ui-kit/pulls/f022064).
- Suppression du bloc de lien "NIS2" dans la suite cyber [#6de23ff](https://github.com/betagouv/lab-anssi-ui-kit/pulls/6de23ff).
- Correction de l'application des props 'fint' et 'radio' sur les éléments radio dans `DsfrRadiosGroup` [#271443a](https://github.com/betagouv/lab-anssi-ui-kit/pulls/271443a).
