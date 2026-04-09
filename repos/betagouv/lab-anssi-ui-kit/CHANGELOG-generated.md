## Changelog : lab-anssi-ui-kit (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, la bibliothèque a bénéficié d'une série d'améliorations axées sur la performance, la sécurité et l'enrichissement des composants. Des correctifs de sécurité ont été appliqués, l'optimisation du bundle a été améliorée, et de nouveaux composants et options de personnalisation ont été ajoutés pour offrir plus de flexibilité aux développeurs. Plusieurs mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la compatibilité.

### Évolutions fonctionnelles
- Ajout du composant `DsfrNotice` pour afficher des messages d'information ou d'alerte. [#81b185f](https://github.com/betagouv/lab-anssi-ui-kit/commit/81b185f)
- Le composant `DsfrCheckbox` dispose maintenant d'un slot `hint` pour ajouter une aide contextuelle. [#633d112](https://github.com/betagouv/lab-anssi-ui-kit/commit/633d112)
- Le composant `DsfrLink` a reçu une nouvelle prop `neutral` pour modifier son apparence. [#c7d38ae](https://github.com/betagouv/lab-anssi-ui-kit/commit/c7d38ae)
- Le composant `DsfrFooter` permet désormais d'ajouter une description via un nouveau slot. [#05a842b](https://github.com/betagouv/lab-anssi-ui-kit/commit/05a842b)
- Le composant `DsfrStepper` permet de masquer les détails avec la prop `hideDetails`. [#63f0e0e](https://github.com/betagouv/lab-anssi-ui-kit/commit/63f0e0e)
- Le composant `DsfrRange` permet de masquer le label de sortie avec la prop `hideOutputLabel`. [#eee6764](https://github.com/betagouv/lab-anssi-ui-kit/commit/eee6764)
- Le composant `DsfrBadgesGroup` prend désormais en compte les champs `icon` et `hasIcon`. [#71e7f58](https://github.com/betagouv/lab-anssi-ui-kit/commit/71e7f58)
- Correction de l'affichage des icônes. [#2f99f4e](https://github.com/betagouv/lab-anssi-ui-kit/commit/2f99f4e)
- Correction du mode téléchargement du `dsfr-link`. [#b9ed0ef](https://github.com/betagouv/lab-anssi-ui-kit/commit/b9ed0ef)

### Évolutions techniques
- Optimisation du bundle grâce au partage des styles d'icônes DSFR via `adoptedStyleSheets`, améliorant ainsi les performances. [#2899155](https://github.com/betagouv/lab-anssi-ui-kit/commit/2899155)
- Refactorisation des composants pour utiliser la fonction `withIconsStyleSheet`. [#1f03fb4](https://github.com/betagouv/lab-anssi-ui-kit/commit/1f03fb4)
- Optimisation des imports CSS des composants DSFR pour utiliser les versions `.main`. [#5ac21b8](https://github.com/betagouv/lab-anssi-ui-kit/commit/5ac21b8)
- Remplacement des imports Core par des imports ciblés dans plusieurs composants (`DsfrLink`, `DsfrBreadcrumb`, `DsfrRange`). [#84c0edd, #741e910, #195257e](https://github.com/betagouv/lab-anssi-ui-kit/commits)
- Mise à jour des dépendances : Svelte (5.55.0), TypeScript (6.0.2), Storybook (10.3.3), Vitest (4.1.1), DSFR (1.14.4). [#6b96626, #880b624, #654d7b0, #b29cdff, #15f4801]
- Application des patchs de sécurité suite aux alertes dependabot. [#c63aaef, #d88cbe1](https://github.com/betagouv/lab-anssi-ui-kit/commit/c63aaef)

### Autres changements
- Amélioration de l'affichage du code source des webcomponents dans la page Autodocs des stories. [#9b604de](https://github.com/betagouv/lab-anssi-ui-kit/commit/9b604de)
- Suppression du bloc de lien "NIS2". [#6de23ff](https://github.com/betagouv/lab-anssi-ui-kit/commit/6de23ff)
- Modification du mixin `set-shadow-host` pour piloter l'application du `font-size` dans `DsfrLink`. [#1d1f2ec](https://github.com/betagouv/lab-anssi-ui-kit/commit/1d1f2ec)
- Amélioration de la gestion de l'attribut `data-themeable` dans `DsfrHeader` et `setThemeable`. [#9ea4a47, #7e79174](https://github.com/betagouv/lab-anssi-ui-kit/commit/9ea4a47)
- Correction de l'application des props `fint` et `radio` sur les éléments radio dans `DsfrRadiosGroup`. [#271443a](https://github.com/betagouv/lab-anssi-ui-kit/commit/271443a)
- Suppression des déclarations de police inutiles. [#f240fd0](https://github.com/betagouv/lab-anssi-ui-kit/commit/f240fd0)
- Suppression des imports inutiles des variables DSFR. [#5afdf9b](https://github.com/betagouv/lab-anssi-ui-kit/commit/5afdf9b)
- Revert d'une modification de la publication NPM. [#f022064](https://github.com/betagouv/lab-anssi-ui-kit/commit/f022064)
