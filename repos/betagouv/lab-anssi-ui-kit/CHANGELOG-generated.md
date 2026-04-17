## Changelog : lab-anssi-ui-kit (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'enrichir la bibliothèque de composants avec l'ajout de nouveaux éléments (onglets, notices, etc.) et des améliorations significatives sur les composants existants, notamment le Header et les liens. Des optimisations de performance ont été apportées pour réduire la taille des bundles et améliorer la vitesse de chargement. Des corrections de sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout du composant `DsfrTabs` et `DsfrTabnav` pour la création d'onglets.
- Ajout du composant `DsfrNotice` pour afficher des messages d'information.
- Ajout d'un slot `hint` au composant `DsfrCheckbox` pour ajouter une aide contextuelle.
- Ajout d'un slot `description` au composant `DsfrFooter` pour personnaliser sa description.
- Le composant `DsfrHeader` a été amélioré avec l'ajout de slots pour personnaliser la barre de navigation et les liens d'outils, ainsi que la gestion des ToolLinks via une prop dédiée. Une story d'exemple pour le Header MSS a également été ajoutée.
- Le composant `DsfrSegmented` a vu son layout responsive amélioré.
- Ajout de la prop `neutral` au composant `DsfrLink`.
- Ajout de la prop `hideDetails` au composant `DsfrStepper`.
- Correction de l'application des props `fint` et `radio` sur les éléments radio du composant `DsfrRadiosGroup`.
- Correction du mode téléchargement du composant `dsfr-link` [#b9ed0ef](https://github.com/betagouv/lab-anssi-ui-kit/commit/b9ed0ef).
- Ajout de l'attribut `id` au composant `DsfrTag`.
- Ajout de l'attribut `data-themeable` avec la valeur `false` sur les boutons du composant `DsfrHeader`.

### Évolutions techniques
- Optimisation de la taille des bundles grâce au partage des styles d'icônes DSFR via `adoptedStyleSheets`.
- Refactorisation des composants pour utiliser la fonction `withIconsStyleSheet`.
- Optimisation des imports CSS des composants DSFR pour utiliser les versions `.main`.
- Remplacement des imports Core par des imports ciblés dans plusieurs composants (DsfrLink, DsfrBreadcrumb, DsfrRange).
- Suppression des déclarations de police inutiles et des imports de variables DSFR inutiles.
- Mise à jour des dépendances :
    - Vitest vers la version 4.1.1
    - TypeScript vers la version 6.0.2
    - Storybook vers la version 10.3.3
    - DSFR vers la version 1.14.4
    - Svelte vers la version 5.55.0
- Application des patchs de sécurité suite aux alertes dependabot.
- Correction d'un problème lié à `follow-redirects`.
- Rétractation d'un changement concernant la publication de packages NPM [#f022064](https://github.com/betagouv/lab-anssi-ui-kit/commit/f022064).

### Autres changements
- Amélioration de la lisibilité des descriptions des slots dans les stories.
- Ajout des descriptions des slots dans les stories.
- Amélioration de l'affichage du code source des webcomponents dans la page Autodocs des stories.
- Modification du mixin 'set-shadow-host' pour piloter l'application du 'font-size' dans le composant `DsfrLink`.
- Modification du passage des tools links en JSON dans le composant `DsfrHeader`.
- Mise à jour des appels à la mixin `set-shadow-host`.
- Amélioration de la gestion de l'attribut `data-themeable` dans la fonction `setThemeable`.
