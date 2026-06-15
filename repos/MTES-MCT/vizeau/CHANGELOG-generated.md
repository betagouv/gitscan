## Changelog : vizeau (30 derniers jours, au 11 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur l'interface utilisateur, notamment avec la création d'une page dédiée aux projets et une vue synthétique de la qualité de l'eau. Des fonctionnalités de gestion des projets ont été ajoutées, comme la possibilité d'assigner des territoires aux exploitations et d'attacher des éléments (exploitations, parcelles, captages) aux projets. Des outils en ligne de commande ont également été ajoutés pour faciliter l'administration et le seeding de données.

### Évolutions fonctionnelles
- Ajout d'une page "Projets" avec une vue "en construction" et une pagination. [#426](https://github.com/MTES-MCT/vizeau/pull/426)
- Création d'une vue synthétique de la qualité de l'eau. [#424](https://github.com/MTES-MCT/vizeau/pull/424)
- Possibilité d'assigner un AAC (Autorité d'Aménagement des Cours d'eau) à une exploitation lors de sa création. [#440](https://github.com/MTES-MCT/vizeau/pull/440)
- Amélioration de la recherche d'AACs. [#439](https://github.com/MTES-MCT/vizeau/pull/439)
- Possibilité d'attacher des exploitations, des parcelles et des captages aux projets. [#425](https://github.com/MTES-MCT/vizeau/pull/425)
- Ajout de commandes en ligne de commande pour le seeding d'utilisateurs et de territoires. [#422](https://github.com/MTES-MCT/vizeau/pull/422)
- Ajout d'une commande pour réinitialiser le mot de passe d'un utilisateur. [#434](https://github.com/MTES-MCT/vizeau/pull/434)
- Amélioration de la visualisation du suivi des substances (correction de l'affichage des unités et du tri). [#407](https://github.com/MTES-MCT/vizeau/pull/407)
- Amélioration du design des substances. [#419](https://github.com/MTES-MCT/vizeau/pull/419)

### Évolutions techniques
- Refactorisation des filtres. [#435](https://github.com/MTES-MCT/vizeau/pull/435)
- Mise à jour de la CI pour utiliser Node 24. [#433](https://github.com/MTES-MCT/vizeau/pull/433)
- Corrections de mocks et amélioration de la gestion d'erreur lors de l'export CSV. [#432](https://github.com/MTES-MCT/vizeau/pull/432)
- Migration des modèles, services et migrations de gestion des étapes de projet. [#410](https://github.com/MTES-MCT/vizeau/pull/410)
- Création d'un composant `SingleSelectMenu`. [#409](https://github.com/MTES-MCT/vizeau/pull/409)
- Remplacement du composant `Select` du DSFR par `SingleSelectMenu`.
- Ajout de la gestion de l'événement `onClick` dans le composant `ListItem`.
- Ajout de la gestion des tags dans le composant `CheckboxCard`.

### Autres changements
- Mise à jour de la documentation de migration en production. [#433](https://github.com/MTES-MCT/vizeau/pull/433)
- Ajout de la documentation de la commande de réinitialisation du mot de passe. [#433](https://github.com/MTES-MCT/vizeau/pull/433)
- Corrections diverses et améliorations du code suite aux revues.
- Corrections de tests unitaires et d'intégration.
- Suppression de code inutile et nettoyage du code.
