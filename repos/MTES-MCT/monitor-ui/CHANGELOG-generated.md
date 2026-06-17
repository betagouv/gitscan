## Changelog : monitor-ui (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration du composant `Dialog`, en corrigeant des problèmes d'affichage et en ajoutant de nouvelles fonctionnalités pour une meilleure expérience utilisateur. De plus, une nouvelle icône a été ajoutée et des dépendances ont été mises à jour pour assurer la stabilité et la sécurité du projet.

### Évolutions fonctionnelles
- Ajout d'une nouvelle icône "fishery crossed" (carrée barrée) pour les icônes. [#196be3bf](https://github.com/MTES-MCT/monitor-ui/commit/96be3bf4661f79f67995c52d922a752493725244)
- Ajout d'un bouton "caution" pour signaler des alertes ou des avertissements. [#9160699](https://github.com/MTES-MCT/monitor-ui/commit/9160699da7fdb20640390622c77084969a63c6a3)

### Évolutions techniques
- Amélioration du composant `Dialog` :
    - Correction de la hauteur maximale du `Dialog`. [#5b34004](https://github.com/MTES-MCT/monitor-ui/commit/5b340043859cdd194f36ae3334f33e37a0cc7f0b)
    - Correction de la largeur du `Dialog`. [#1c98223](https://github.com/MTES-MCT/monitor-ui/commit/1c982234a8bbd85b3fe82b83cf351c6fc122b456)
    - Ajout du titre au bouton de fermeture du `Dialog`. [#09a758d](https://github.com/MTES-MCT/monitor-ui/commit/09a758d1f9dd2c744e7c539b81c7175b7d14c8dc)
    - Correction de la taille de la police dans le corps du `Dialog`. [#5bcd0fc](https://github.com/MTES-MCT/monitor-ui/commit/5bcd0fce3686a7be776d193901786318c58133ee)
    - Possibilité d'ajouter des enfants au titre du `Dialog`. [#bade645](https://github.com/MTES-MCT/monitor-ui/commit/bade645291421839c9383da904468c2b019c189d) et [#5d18af6](https://github.com/MTES-MCT/monitor-ui/commit/5d18af63d27560c6d12fed3044a0c1a39e75c191)
- Mise à jour de la configuration de Dependabot pour améliorer la gestion des dépendances. [#babb4c5](https://github.com/MTES-MCT/monitor-ui/commit/babb4c5509e8f204f1a4b7963ff0fbb4dafcf652)
- Désactivation du rebasage automatique de Dependabot. [#986a64a](https://github.com/MTES-MCT/monitor-ui/commit/986a64a9b1faa7e5b2d1454769f0552e0b839abb)

### Autres changements
- Mise à jour de plusieurs dépendances de développement (ESLint, Storybook, Cypress, etc.).
- Mise à jour des versions de certaines actions GitHub.
- Correction d'erreurs et amélioration de la configuration des dépendances.
