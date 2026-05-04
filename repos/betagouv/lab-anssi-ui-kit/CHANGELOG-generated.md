## Changelog : lab-anssi-ui-kit (30 derniers jours, au 29 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la validation des formulaires, avec l'implémentation de la validation des contraintes HTML pour plusieurs composants. De nouveaux composants DSFR ont été ajoutés, notamment MessagesGroup, User, Tabs et Tabnav. Des améliorations ont également été apportées au composant Header, avec des options de personnalisation plus poussées et des exemples dédiés pour MQC et MSS. Enfin, des corrections et des optimisations diverses ont été réalisées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout du composant `DsfrMessagesGroup` pour afficher des messages d'information ou d'erreur. [#841278f](https://github.com/betagouv/lab-anssi-ui-kit/pull/841278f)
- Ajout du composant `DsfrUser` pour afficher des informations sur un utilisateur. [#d356018](https://github.com/betagouv/lab-anssi-ui-kit/pull/d356018)
- Ajout des composants `DsfrTabs` et `DsfrTabnav` pour créer des interfaces à onglets. [#83edacb](https://github.com/betagouv/lab-anssi-ui-kit/pull/83edacb) et [#198cfa8](https://github.com/betagouv/lab-anssi-ui-kit/pull/198cfa8)
- Amélioration du composant `DsfrHeader` avec des slots pour personnaliser la barre de navigation et les liens d'outils. [#b0e720a](https://github.com/betagouv/lab-anssi-ui-kit/pull/b0e720a) et [#6958024](https://github.com/betagouv/lab-anssi-ui-kit/pull/6958024)
- Ajout d'exemples de composants `Header` pour MQC et MSS. [#feb4328](https://github.com/betagouv/lab-anssi-ui-kit/pull/feb4328) et [#4d04a65](https://github.com/betagouv/lab-anssi-ui-kit/pull/4d04a65)
- Implémentation de la validation des contraintes HTML pour les composants `DsfrCheckbox`, `DsfrCheckboxesGroup`, `DsfrInput`, `DsfrTextarea`, `DsfrSelect`, `DsfrSearch`, `DsfrRadiosGroup`. [#f916fb4](https://github.com/betagouv/lab-anssi-ui-kit/pull/f916fb4), [#b16e557](https://github.com/betagouv/lab-anssi-ui-kit/pull/b16e557), [#a098657](https://github.com/betagouv/lab-anssi-ui-kit/pull/a098657), [#9e5eac1](https://github.com/betagouv/lab-anssi-ui-kit/pull/9e5eac1), [#9333c7a](https://github.com/betagouv/lab-anssi-ui-kit/pull/9333c7a), [#5727e92](https://github.com/betagouv/lab-anssi-ui-kit/pull/5727e92), [#43164a5](https://github.com/betagouv/lab-anssi-ui-kit/pull/43164a5), [#36c32c3](https://github.com/betagouv/lab-anssi-ui-kit/pull/36c32c3)
- Correction des breakpoints de la `NavigationSuiteCyber`. [#a091cc6](https://github.com/betagouv/lab-anssi-ui-kit/pull/a091cc6)
- Affichage du statut "actif" des sous-items de la navigation. [#98de9f2](https://github.com/betagouv/lab-anssi-ui-kit/pull/98de9f2)

### Évolutions techniques
- Refactoring : Extraction de la logique de validation dans une fonction externe. [#9e5eac1](https://github.com/betagouv/lab-anssi-ui-kit/pull/9e5eac1)
- Mise à jour des dépendances obsolètes. [#0d0355c](https://github.com/betagouv/lab-anssi-ui-kit/pull/0d0355c)
- Application d'un patch de sécurité concernant 'follow-redirects'. [#5ff3d76](https://github.com/betagouv/lab-anssi-ui-kit/pull/5ff3d76)
- Correction du passage de la prop 'inline' au composant `DsfrButtonsGroup`. [#f7833b1](https://github.com/betagouv/lab-anssi-ui-kit/pull/f7833b1)
- Rendre la prop 'label' du bouton optionnel. [#fe708d7](https://github.com/betagouv/lab-anssi-ui-kit/pull/fe708d7)
- Amélioration de la gestion du layout responsive du composant `DsfrSegmented`. [#670fd88](https://github.com/betagouv/lab-anssi-ui-kit/pull/670fd88)
- Mise à jour des appels à la mixin `set-shadow-host`. [#59841a8](https://github.com/betagouv/lab-anssi-ui-kit/pull/59841a8)

### Autres changements
- Ajout d'une story d'exemple pour la validation des formulaires. [#41181ef](https://github.com/betagouv/lab-anssi-ui-kit/pull/41181ef)
- Ajout d'un slot pour insérer une image personnalisée dans le composant `DsfrCard`. [#9911bac](https://github.com/betagouv/lab-anssi-ui-kit/pull/9911bac)
- Inversion de la position du slot 'contentend' dans le composant `DsfrCard`. [#0dad2f1](https://github.com/betagouv/lab-anssi-ui-kit/pull/0dad2f1)
- Ajout de l'attribut 'id' pour le tag dans le composant `DsfrTag`. [#0ead556](https://github.com/betagouv/lab-anssi-ui-kit/pull/0ead556)
- Ajout des descriptions des slots dans les stories. [#b53a03e](https://github.com/betagouv/lab-anssi-ui-kit/pull/b53a03e) et [#7087728](https://github.com/betagouv/lab-anssi-ui-kit/pull/7087728)
- Ajout de styles de fallback pour le conteneur dsfr. [#29fecba](https://github.com/betagouv/lab-anssi-ui-kit/pull/29fecba)
- Remplacement des citations LAB par les citations DSFR. [#7b24ea6](https://github.com/betagouv/lab-anssi-ui-kit/pull/7b24ea6)
- Correction du type de l'attribut 'alt' et ajustement des valeurs par défaut dans le composant `DsfrCard`. [#26e2d22](https://github.com/betagouv/lab-anssi-ui-kit/pull/26e2d22)
- Ajout du type et du statut aux badges dans le composant `DsfrBadgesGroup`. [#fd0f385](https://github.com/betagouv/lab-anssi-ui-kit/pull/fd0f385)
- Modification du passage des tools links en JSON dans le composant `DsfrHeader`. [#5f87a35](https://github.com/betagouv/lab-anssi-ui-kit/pull/5f87a35)
- Suppression du bloc de lien "NIS2". [#6de23ff](https://github.com/betagouv/lab-anssi-ui-kit/pull/6de23ff)
- Revert d'une modification concernant la publication npm. [#f022064](https://github.com/betagouv/lab-anssi-ui-kit/pull/f022064)
