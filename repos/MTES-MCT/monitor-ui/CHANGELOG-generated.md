## Changelog : monitor-ui (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le composant Dialog, avec des corrections de taille, de police et de gestion des titres. Une nouvelle icône "Lock" a été ajoutée et un bouton "Caution" a été implémenté. Des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité du projet.

### Évolutions fonctionnelles
- Ajout d'une nouvelle icône "Lock" pour une utilisation dans l'interface utilisateur. [#96be3bf](https://github.com/MTES-MCT/monitor-ui/commit/96be3bf)
- Implémentation d'un nouveau bouton "Caution" pour signaler des actions potentiellement risquées. [#9160699](https://github.com/MTES-MCT/monitor-ui/commit/9160699)
- Amélioration du composant `Dialog` :
    - Correction de la hauteur maximale pour éviter des problèmes d'affichage. [#5b34004](https://github.com/MTES-MCT/monitor-ui/commit/5b340043859cdd194f36ae3334f33e37a0cc7f0b)
    - Correction de la largeur du composant. [#1c98223](https://github.com/MTES-MCT/monitor-ui/commit/1c982234a8bbd85b3fe82b83cf351c6fc122b456)
    - Amélioration de la gestion des titres, permettant d'ajouter des enfants au titre. [#bade645](https://github.com/MTES-MCT/monitor-ui/commit/bade645291421839c9383da904468c2b019c189d) et [#5d18af6](https://github.com/MTES-MCT/monitor-ui/commit/5d18af63d27560c6d12fed3044a0c1a39e75c191)
    - Correction de la taille de la police dans le corps du dialogue. [#5bcd0fc](https://github.com/MTES-MCT/monitor-ui/commit/5bcd0fce3686a7be776d193901786318c58133ee)
- Correction d'un export dans les composants. [#6ef0c8d](https://github.com/MTES-MCT/monitor-ui/commit/6ef0c8d4f559416660964f2759f588186166b896)
- Possibilité de rendre les options de tableau plus facilement remplaçables. [#258e232](https://github.com/MTES-MCT/monitor-ui/commit/258e23260763f65929659725587a7962994a1779)

### Évolutions techniques
- Mise à jour des dépendances de développement (eslint-plugin-mocha, glob, storybook, cypress-io/github-action) et des dépendances générales.
- Configuration de Dependabot pour éviter les auto-rebase. [#986a64a](https://github.com/MTES-MCT/monitor-ui/commit/986a64a9b1faa7e5b2d1454769f0552e0b839abb)
- Mise à jour de la configuration de Dependabot. [#babb4c5](https://github.com/MTES-MCT/monitor-ui/commit/babb4c5509e8f204f1a4b7963ff0fbb4dafcf652)
- Mises à jour des versions de GitHub Actions. [#175c380](https://github.com/MTES-MCT/monitor-ui/commit/175c380ad8b2de2df964c80f2d863bea4ffc5f3f)

### Autres changements
- Correction d'un bouton de fermeture dans le composant Dialog pour améliorer l'accessibilité. [#09a758d](https://github.com/MTES-MCT/monitor-ui/commit/09a758d1f9dd2c744e7c539b81c7175b7d14c8dc)
