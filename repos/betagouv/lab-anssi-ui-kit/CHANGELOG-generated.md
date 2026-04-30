## Changelog : lab-anssi-ui-kit (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'enrichir la bibliothèque de composants avec l'ajout de nouveaux éléments (User, Tabs, Notice, etc.) et l'amélioration de ceux existants (Header, Card, Checkbox, etc.). Un effort important a été réalisé pour améliorer la validation des formulaires et la gestion des thèmes, ainsi que pour corriger des bugs et mettre à jour les dépendances.

### Évolutions fonctionnelles
- Ajout du composant `DsfrUser` pour afficher des informations sur un utilisateur. [#d356018](https://github.com/betagouv/lab-anssi-ui-kit/issues/d356018)
- Ajout des composants `DsfrTabs` et `DsfrTabnav` pour créer des interfaces à onglets. [#83edacb](https://github.com/betagouv/lab-anssi-ui-kit/issues/83edacb) et [#198cfa8](https://github.com/betagouv/lab-anssi-ui-kit/issues/198cfa8)
- Ajout du composant `DsfrNotice` pour afficher des messages d'information ou d'alerte. [#81b185f](https://github.com/betagouv/lab-anssi-ui-kit/issues/81b185f)
- Ajout d'un slot 'hint' au composant `DsfrCheckbox` pour ajouter une aide contextuelle. [#633d112](https://github.com/betagouv/lab-anssi-ui-kit/issues/633d112)
- Amélioration du composant `DsfrHeader` avec l'ajout de slots pour personnaliser la barre de navigation et les liens d'outils, ainsi que la gestion des ToolLinks et d'un conteneur fluide. [#b0e720a](https://github.com/betagouv/lab-anssi-ui-kit/issues/b0e720a), [#6958024](https://github.com/betagouv/lab-anssi-ui-kit/issues/6958024), [#4630979](https://github.com/betagouv/lab-anssi-ui-kit/issues/4630979)
- Ajout d'un slot pour insérer une image personnalisée dans le composant `DsfrCard`. [#9911bac](https://github.com/betagouv/lab-anssi-ui-kit/issues/9911bac)
- Ajout de la prop 'neutral' au composant `DsfrLink`. [#c7d38ae](https://github.com/betagouv/lab-anssi-ui-kit/issues/c7d38ae)
- Ajout d'un slot 'description' au composant `DsfrFooter`. [#05a842b](https://github.com/betagouv/lab-anssi-ui-kit/issues/05a842b)
- Implémentation de la validation des contraintes HTML pour les composants `DsfrCheckbox`, `DsfrCheckboxesGroup`, `DsfrInput`, `DsfrTextarea`, `DsfrSelect`, `DsfrSearch` et `DsfrRadiosGroup`. [#f916fb4](https://github.com/betagouv/lab-anssi-ui-kit/issues/f916fb4), [#b16e557](https://github.com/betagouv/lab-anssi-ui-kit/issues/b16e557), [#a098657](https://github.com/betagouv/lab-anssi-ui-kit/issues/a098657), [#9e5eac1](https://github.com/betagouv/lab-anssi-ui-kit/issues/9e5eac1), [#9333c7a](https://github.com/betagouv/lab-anssi-ui-kit/issues/9333c7a), [#5727e92](https://github.com/betagouv/lab-anssi-ui-kit/issues/5727e92), [#36c32c3](https://github.com/betagouv/lab-anssi-ui-kit/issues/36c32c3)
- Association des composants DSFR aux formulaires web natifs. [#90ca630](https://github.com/betagouv/lab-anssi-ui-kit/issues/90ca630) et [#1309779](https://github.com/betagouv/lab-anssi-ui-kit/issues/1309779)

### Évolutions techniques
- Mise à jour des dépendances : Vitest (v4.1.1), TypeScript (v6.0.2), Storybook (v10.3.3), Svelte (v5.55.0), DSFR (v1.14.4). [#b29cdff](https://github.com/betagouv/lab-anssi-ui-kit/issues/b29cdff), [#880b624](https://github.com/betagouv/lab-anssi-ui-kit/issues/880b624), [#6b96626](https://github.com/betagouv/lab-anssi-ui-kit/issues/6b96626), [#5ba71b2](https://github.com/betagouv/lab-anssi-ui-kit/issues/5ba71b2), [#15f4801](https://github.com/betagouv/lab-anssi-ui-kit/issues/15f4801)
- Refactoring pour utiliser la fonction `withIconsStyleSheet`. [#1f03fb4](https://github.com/betagouv/lab-anssi-ui-kit/issues/1f03fb4)
- Extraction de la logique de validation dans une fonction externe. [#9e5eac1](https://github.com/betagouv/lab-anssi-ui-kit/issues/9e5eac1)
- Application des patchs de sécurité suite aux alertes dependabot. [#c63aaef](https://github.com/betagouv/lab-anssi-ui-kit/issues/c63aaef) et [#d88cbe1](https://github.com/betagouv/lab-anssi-ui-kit/issues/d88cbe1)
- Application du patch de sécurité concernant 'follow-redirects'. [#5ff3d76](https://github.com/betagouv/lab-anssi-ui-kit/issues/5ff3d76)

### Autres changements
- Ajout de stories d'exemple pour la validation des formulaires et les Headers MSS (connecté et non connecté). [#41181ef](https://github.com/betagouv/lab-anssi-ui-kit/issues/41181ef), [#4d04a65](https://github.com/betagouv/lab-anssi-ui-kit/issues/4d04a65), [#feb4328](https://github.com/betagouv/lab-anssi-ui-kit/issues/feb4328)
- Ajout de descriptions des slots dans les stories. [#b53a03e](https://github.com/betagouv/lab-anssi-ui-kit/issues/b53a03e) et [#7087728](https://github.com/betagouv/lab-anssi-ui-kit/issues/7087728)
- Correction des breakpoints de la `NavigationSuiteCyber`. [#a091cc6](https://github.com/betagouv/lab-anssi-ui-kit/issues/a091cc6)
- Affichage du statut "actif" des sous-items de la navigation. [#98de9f2](https://github.com/betagouv/lab-anssi-ui-kit/issues/98de9f2)
- Remplacement des citations LAB par les citations DSFR. [#7b24ea6](https://github.com/betagouv/lab-anssi-ui-kit/issues/7b24ea6)
- Ajout de styles de fallback pour le conteneur DSFR. [#29fecba](https://github.com/betagouv/lab-anssi-ui-kit/issues/29fecba)
- Inversion de la position du slot 'contentend' dans `DsfrCard`. [#0dad2f1](https://github.com/betagouv/lab-anssi-ui-kit/issues/0dad2f1)
- Correction du passage de la prop 'inline' au composant `DsfrButtonsGroup`. [#f7833b1](https://github.com/betagouv/lab-anssi-ui-kit/issues/f7833b1)
- Rendre la prop 'label' du bouton optionnel. [#fe708d7](https://github.com/betagouv/lab-anssi-ui-kit/issues/fe708d7)
- Ajout d'une condition à l'affichage du service de marque dans `DsfrHeader`. [#4a155e9](https://github.com/betagouv/lab-anssi-ui-kit/issues/4a155e9)
- Amélioration du mode de calcul de la hauteur des onglets dans `DsfrTabs`. [#8f64c67](https://github.com/betagouv/lab-anssi-ui-kit/issues/8f64c67)
- Amélioration de la gestion du layout responsive dans `DsfrSegmented`. [#670fd88](https://github.com/betagouv/lab-anssi-ui-kit/issues/670fd88)
- Correction du type de l'attribut 'alt' et ajustement des valeurs par défaut dans `DsfrCard`. [#26e2d22](https://github.com/betagouv/lab-anssi-ui-kit/issues/26e2d22)
- Ajout du type et du statut aux badges dans `DsfrBadgesGroup`. [#fd0f385](https://github.com/betagouv/lab-anssi-ui-kit/issues/fd0f385)
- Suppression du bloc de lien "NIS2" dans la suite cyber. [#6de23ff](https://github.com/betagouv/lab-anssi-ui-kit/issues/6de23ff)
- Revert de la modification autorisant la publication npm autre que 'latest'. [#f022064](https://github.com/betagouv/lab-anssi-ui-kit/issues/f022064)
