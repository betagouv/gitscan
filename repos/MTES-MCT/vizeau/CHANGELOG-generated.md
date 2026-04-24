## Changelog : vizeau (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, Vizeau a bénéficié d'améliorations significatives en termes de gestion des exploitations agricoles, notamment avec l'ajout de fonctionnalités d'export de données (exploitations, journaux de bord) et de gestion des territoires pour les utilisateurs. L'interface utilisateur a également été enrichie avec de nouvelles couches cartographiques, des informations sur les AAC et des corrections pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les parcelles d'une exploitation [#372](https://github.com/MTES-MCT/vizeau/issues/372).
- Implémentation de l'export du journal de bord d'une exploitation [#371](https://github.com/MTES-MCT/vizeau/issues/371).
- Possibilité d'assigner des territoires aux utilisateurs via une commande CLI dédiée [#358](https://github.com/MTES-MCT/vizeau/issues/358) et [#359](https://github.com/MTES-MCT/vizeau/issues/359).
- Gestion des permissions par territoire : les utilisateurs sont redirigés vers l'accueil s'ils n'ont pas accès à un territoire [#358](https://github.com/MTES-MCT/vizeau/issues/358).
- Amélioration de la visualisation des AAC avec l'ajout d'un résumé des informations et un centrage sur la carte [#357](https://github.com/MTES-MCT/vizeau/issues/357).
- Ajout de nouvelles couches sur la carte de visualisation [#366](https://github.com/MTES-MCT/vizeau/issues/366).
- Ajout d'une indication de RPG (Régime de Production Générale) [#357](https://github.com/MTES-MCT/vizeau/issues/357).
- Traduction des codes NAF en libellés [#370](https://github.com/MTES-MCT/vizeau/issues/370).
- Correction de la gestion inter-formulaires et de la suppression du dernier contact supplémentaire dans le formulaire de contact secondaire [#363](https://github.com/MTES-MCT/vizeau/issues/363).
- Ajout des bounding boxes (bbox) sur les fiches AAC [#354](https://github.com/MTES-MCT/vizeau/issues/354).
- Amélioration de la réactivité de la section répartition [#355](https://github.com/MTES-MCT/vizeau/issues/355).

### Évolutions techniques
- Composants pour le module "Point de prélèvement" [#381](https://github.com/MTES-MCT/vizeau/issues/381).
- Correction de la transparence des résultats dans le composant autocomplete [#378](https://github.com/MTES-MCT/vizeau/issues/378).
- Mise à jour des mini-cartes [#350](https://github.com/MTES-MCT/vizeau/issues/350).
- Filtrage des AACs dans la page de visualisation [#364](https://github.com/MTES-MCT/vizeau/issues/364).
- Correction de la requête d'affichage du journal de bord sur la page d'accueil.

### Autres changements
- Seeding des comptes animateurs avec attribution de territoire [#380](https://github.com/MTES-MCT/vizeau/issues/380).
- Seed des territoires aux utilisateurs [#375](https://github.com/MTES-MCT/vizeau/issues/375).
- Diverses corrections et optimisations suite aux revues de code Copilot.
- Corrections diverses et améliorations de la gestion des dépendances.
