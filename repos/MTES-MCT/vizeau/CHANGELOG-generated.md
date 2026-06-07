## Changelog : vizeau (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la gestion des projets, avec la création d'une page dédiée et l'ajout de fonctionnalités permettant d'attacher des exploitations, parcelles et captages aux projets. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour le suivi des substances et la visualisation de la qualité de l'eau. Enfin, des outils en ligne de commande ont été ajoutés pour faciliter la gestion des territoires et des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une page "en construction" pour la page projet, en préparation de son déploiement complet. [#426](https://github.com/MTES-MCT/vizeau/pull/426)
- Implémentation de la gestion des étapes de projet, permettant de suivre l'avancement des projets. [#429](https://github.com/MTES-MCT/vizeau/pull/429)
- Possibilité d'attacher des exploitations, parcelles et captages aux projets. [#425](https://github.com/MTES-MCT/vizeau/pull/425) et [#433](https://github.com/MTES-MCT/vizeau/pull/433)
- Ajout d'une vue synthétique de la qualité de l'eau. [#424](https://github.com/MTES-MCT/vizeau/pull/424)
- Amélioration de la visualisation du suivi des substances, avec un nouveau composant `SingleSelectMenu`. [#409](https://github.com/MTES-MCT/vizeau/pull/409) et [#419](https://github.com/MTES-MCT/vizeau/pull/419)
- Ajout d'un CTA (Call To Action) sur les cartes de résumé. [#419](https://github.com/MTES-MCT/vizeau/pull/419)
- Correction de l'affichage des couleurs dans la répartition des cultures. [#431](https://github.com/MTES-MCT/vizeau/issues/431)
- Correction de l'affichage de l'évolution des parcelles bio (passage de % à ha). [#428](https://github.com/MTES-MCT/vizeau/issues/428)
- Ajout d'un toaster de confirmation lors de l'attribution des parcelles. [#403](https://github.com/MTES-MCT/vizeau/issues/403)
- Tri des substances affichées dans la liste déroulante. [#407](https://github.com/MTES-MCT/vizeau/issues/407)

### Évolutions techniques
- Mise à jour de la version de Node.js utilisée par la CI à Node 24. [#432](https://github.com/MTES-MCT/vizeau/pull/432)
- Amélioration de la gestion d'erreur et corrections de mocks lors de l'export CSV. [#432](https://github.com/MTES-MCT/vizeau/pull/432)
- Ajout de commandes en ligne de commande pour le seeding d'utilisateurs et de territoires. [#405](https://github.com/MTES-MCT/vizeau/pull/405) et [#410](https://github.com/MTES-MCT/vizeau/pull/410)
- Refactoring et implémentation du backend pour la gestion des projets. [#405](https://github.com/MTES-MCT/vizeau/pull/405)
- Mise à jour du service de recherche d'exploitations. [#404](https://github.com/MTES-MCT/vizeau/issues/404)
- Correction d'une mauvaise requête SQL. [#422](https://github.com/MTES-MCT/vizeau/pull/422)

### Autres changements
- Corrections mineures sur les éléments de liste.
- Validation des entrées.
- Pagination implémentée.
- Suppression du retour JSON inutile.
- Déplacement des modèles de type de ProjetsTabs.
- Corrections et améliorations diverses suite aux revues de code (Copilot).
- Ajout d'attributs manquants et corrections de padding.
