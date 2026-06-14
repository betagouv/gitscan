## Changelog : monitor-ui (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le composant Dialog, avec des corrections de bugs concernant la taille, la police et l'ajout d'un titre cliquable pour la fermeture. Une nouvelle icône "Lock" a été ajoutée et un bouton d'avertissement a été créé. Des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité du projet.

### Évolutions fonctionnelles
- Ajout d'une nouvelle icône "Lock" pour une utilisation dans l'interface utilisateur. [#96be3bf](https://github.com/MTES-MCT/monitor-ui/commit/96be3bf)
- Création d'un nouveau bouton "caution" pour signaler des actions potentiellement risquées. [#9160699](https://github.com/MTES-MCT/monitor-ui/commit/9160699)
- Amélioration du composant `Dialog` :
    - Correction du titre pour permettre l'ajout d'enfants. [#bade645](https://github.com/MTES-MCT/monitor-ui/commit/bade645)
    - Correction de la taille (largeur et hauteur maximale). [#1c98223](https://github.com/MTES-MCT/monitor-ui/commit/1c98223), [#5b34004](https://github.com/MTES-MCT/monitor-ui/commit/5b34004)
    - Correction de la taille de la police dans le corps du dialogue. [#5bcd0fc](https://github.com/MTES-MCT/monitor-ui/commit/5bcd0fc)
    - Ajout d'un titre cliquable pour fermer la fenêtre de dialogue. [#09a758d](https://github.com/MTES-MCT/monitor-ui/commit/09a758d)

### Évolutions techniques
- Mise à jour de plusieurs dépendances de développement (ESLint, Storybook, Cypress, etc.) pour bénéficier des dernières corrections et améliorations.
- Mise à jour de certaines dépendances principales (lodash-es, vite, postcss).
- Configuration de Dependabot pour désactiver le rebasage automatique. [#986a64a](https://github.com/MTES-MCT/monitor-ui/commit/986a64a)

### Autres changements
- Mise à jour de la configuration de Dependabot. [#babb4c5](https://github.com/MTES-MCT/monitor-ui/commit/babb4c5)
- Correction d'une exportation dans un composant. [#6ef0c8d](https://github.com/MTES-MCT/monitor-ui/commit/6ef0c8d)
