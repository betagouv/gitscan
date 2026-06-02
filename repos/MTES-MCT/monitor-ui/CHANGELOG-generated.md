## Changelog : monitor-ui (30 derniers jours, au 1er juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le composant Dialog, avec des corrections de style et des améliorations de la flexibilité. Des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité du projet. Enfin, une nouvelle icône "Lock" a été ajoutée.

### Évolutions fonctionnelles
- Ajout d'une nouvelle icône "Lock" pour une meilleure représentation visuelle des états de sécurité. [#96be3bf](https://github.com/MTES-MCT/monitor-ui/commit/96be3bf2f2906a7f4993f9848626041b43901579)
- Amélioration du composant `Dialog` :
    - Correction de la taille de police du corps du dialogue. [#5bcd0fc](https://github.com/MTES-MCT/monitor-ui/commit/5bcd0fce3686a7be776d193901786318c58133ee)
    - Possibilité d'ajouter des enfants au titre du dialogue. [#5d18af6](https://github.com/MTES-MCT/monitor-ui/commit/5d18af63d27560c6d12fed3044a0c1a39e75c191)
    - Mise à jour générale du composant pour une meilleure flexibilité. [#d2b6f83](https://github.com/MTES-MCT/monitor-ui/commit/d2b6f83a5f4d801d196d0659cd4d475f438c0d19)
- Le composant `Table` a été modifié pour rendre les options de la table plus facilement remplaçables. [#258e232](https://github.com/MTES-MCT/monitor-ui/commit/258e23224961910641936f10a9634493179421d6)

### Évolutions techniques
- Mise à jour des dépendances : Lodash-es, Vite, PostCSS, ainsi que plusieurs dépendances de développement (Storybook, Cypress, ESLint, etc.). [#7573470](https://github.com/MTES-MCT/monitor-ui/commit/75734701246fbe1d11972d3dd416f24dd942ff0e) et autres commits liés aux dépendances.
- Configuration de Dependabot : Désactivation du rebasage automatique pour éviter les conflits. [#986a64a](https://github.com/MTES-MCT/monitor-ui/commit/986a64a9b1faa7e5b2d1454769f0552e0b839abb)
- Mise à jour de la configuration de Dependabot pour une meilleure gestion des dépendances. [#babb4c5](https://github.com/MTES-MCT/monitor-ui/commit/babb4c5509e8f204f1a4b7963ff0fbb4dafcf652)

### Autres changements
- Correction d'une exportation dans les composants. [#6ef0c8d](https://github.com/MTES-MCT/monitor-ui/commit/6ef0c8d679085f65f7947f49909899981914873b)
- Publication des versions 24.49.1, 24.49.2, 24.50.0, 24.50.1 et 24.51.0.
