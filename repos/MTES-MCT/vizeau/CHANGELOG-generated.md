## Changelog : vizeau (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des projets, avec l'ajout de nouvelles fonctionnalités pour la création, l'édition et le suivi des étapes. Des améliorations ont également été apportées à l'interface utilisateur, notamment sur les pages "Mes territoires" et la vue synthétique de la qualité de l'eau. Enfin, des corrections et optimisations techniques ont été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une page "Mes territoires" permettant aux utilisateurs de visualiser et gérer leurs territoires. [#447](https://github.com/MTES-MCT/vizeau/pulls/447)
- Implémentation d'une vue synthétique de la qualité de l'eau. [#424](https://github.com/MTES-MCT/vizeau/pulls/424)
- Création d'une page pour la gestion des projets, incluant la possibilité de créer un nouveau projet. [#441](https://github.com/MTES-MCT/vizeau/pulls/441)
- Ajout de la fonctionnalité d'édition des projets. [#427](https://github.com/MTES-MCT/vizeau/pulls/427)
- Possibilité d'associer des parcelles à un projet via un bouton de navigation dédié. [#452](https://github.com/MTES-MCT/vizeau/pulls/452)
- Ajout de la gestion des étapes de projet : création, édition, suppression et validation. [#451](https://github.com/MTES-MCT/vizeau/pulls/451)
- Possibilité d'attacher des exploitations, parcelles et captages à un projet. [#425](https://github.com/MTES-MCT/vizeau/pulls/425)
- Amélioration de l'affichage de l'évolution des parcelles bio (passage de % à ha). [#428](https://github.com/MTES-MCT/vizeau/pulls/428)
- Correction de l'affichage des couleurs dans la répartition des cultures. [#431](https://github.com/MTES-MCT/vizeau/pulls/431)
- Ajout d'un deeplink pour centrer la vue sur une parcelle spécifique.

### Évolutions techniques
- Raccourcissement des imports relatifs des types pour améliorer la lisibilité du code. [#442](https://github.com/MTES-MCT/vizeau/pulls/442)
- Mise à jour de la CI pour utiliser Node 24. [#432](https://github.com/MTES-MCT/vizeau/pulls/432)
- Refactorisation des filtres pour améliorer la maintenabilité. [#435](https://github.com/MTES-MCT/vizeau/pulls/435)
- Correction d'une mauvaise requête SQL lors de l'attachement des entités aux projets.
- Amélioration de la gestion des erreurs lors de l'export CSV.
- Correction de la gestion des flash messages pour éviter les erreurs liées à la session. [#444](https://github.com/MTES-MCT/vizeau/pulls/444)
- Mise à jour des tests unitaires pour assurer la couverture du code.
- Validation du payload dans le validateur pour garantir l'intégrité des données.

### Autres changements
- Ajout de commandes pour la création d'utilisateurs et la réinitialisation des mots de passe en ligne de commande. [#434](https://github.com/MTES-MCT/vizeau/pulls/434) et [#422](https://github.com/MTES-MCT/vizeau/pulls/422)
- Mise à jour de la documentation de migration en production. [#433](https://github.com/MTES-MCT/vizeau/pulls/433)
- Amélioration de la réactivité de la mise en page de certains composants. [#455](https://github.com/MTES-MCT/vizeau/pulls/455)
- Corrections de linter et de style pour améliorer la qualité du code.
- Suppression de code inutile et simplification de certaines parties de l'application.
- Correction de plusieurs bugs mineurs et améliorations de l'expérience utilisateur.
