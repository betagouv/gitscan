## Changelog : vizeau (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, l'application Vizeau a connu des avancées significatives dans la gestion des projets, avec l'ajout de nouvelles fonctionnalités pour la création, l'édition, la visualisation et l'association de projets à des parcelles et des exploitations. Des améliorations ont également été apportées à l'interface utilisateur et à l'infrastructure technique pour une meilleure expérience et performance.

### Évolutions fonctionnelles
- Ajout d'une page "Mes territoires" permettant de visualiser et gérer les territoires de l'utilisateur. [#444](https://github.com/MTES-MCT/vizeau/pull/444)
- Implémentation de la création et de l'édition de projets, incluant la gestion des étapes. [#447](https://github.com/MTES-MCT/vizeau/pull/447), [#450](https://github.com/MTES-MCT/vizeau/pull/450), [#451](https://github.com/MTES-MCT/vizeau/pull/451)
- Possibilité d'associer des parcelles à un projet via un bouton dédié. [#452](https://github.com/MTES-MCT/vizeau/pull/452)
- Ajout d'une vue synthétique de la qualité de l'eau. [#424](https://github.com/MTES-MCT/vizeau/pull/424)
- Amélioration de l'affichage de l'évolution des parcelles bio (passage de % à ha). [#428](https://github.com/MTES-MCT/vizeau/pull/428)
- Possibilité d'attacher des exploitations, des parcelles et des captages à un projet. [#425](https://github.com/MTES-MCT/vizeau/pull/425)
- Ajout d'une page "En construction" pour les futures fonctionnalités de gestion de projet.
- Ajout de la possibilité de rediriger vers une parcelle spécifique avec centrage sur la carte.

### Évolutions techniques
- Refactorisation des filtres pour une meilleure organisation et maintenabilité. [#435](https://github.com/MTES-MCT/vizeau/pull/435)
- Raccourcissement des imports relatifs des types pour améliorer la lisibilité du code. [#442](https://github.com/MTES-MCT/vizeau/pull/442)
- Mise à jour de la CI pour utiliser Node 24. [#432](https://github.com/MTES-MCT/vizeau/pull/432)
- Amélioration de la gestion des erreurs et des mocks dans les tests.
- Corrections de requêtes SQL pour optimiser les performances.
- Mise en place de validateurs pour les données du projet.
- Migration vers une architecture plus modulaire pour la gestion des étapes de projet. [#429](https://github.com/MTES-MCT/vizeau/pull/429)

### Autres changements
- Ajout de commandes CLI pour la gestion des utilisateurs et la réinitialisation des mots de passe. [#434](https://github.com/MTES-MCT/vizeau/pull/434), [#422](https://github.com/MTES-MCT/vizeau/pull/422)
- Mise à jour de la documentation de migration en production. [#433](https://github.com/MTES-MCT/vizeau/pull/433)
- Amélioration de la gestion des flash messages et de l'accès à la session. [#440](https://github.com/MTES-MCT/vizeau/pull/440)
- Corrections de linter et de style pour améliorer la qualité du code.
- Diverses corrections de bugs et améliorations de l'interface utilisateur.
