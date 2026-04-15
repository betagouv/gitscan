## Changelog : vizeau (30 derniers jours, au 15 avril 2026)

### Résumé
Les dernières mises à jour de Vizeau se concentrent sur l'amélioration de la gestion des données agricoles et de l'eau, notamment avec l'ajout de nouvelles fonctionnalités d'export de données (exploitations, journaux de bord, parcelles), l'enrichissement de la visualisation des données (couches cartographiques, analyses d'eau, évolution des cultures) et l'amélioration de l'interface utilisateur pour une meilleure expérience. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les parcelles d'une exploitation [#372](https://github.com/MTES-MCT/vizeau/pull/372).
- Ajout de la possibilité d'exporter le journal de bord d'une exploitation [#371](https://github.com/MTES-MCT/vizeau/pull/371).
- Traduction des codes NAF en libellés pour une meilleure compréhension [#370](https://github.com/MTES-MCT/vizeau/pull/370).
- Ajout de nouvelles couches sur la carte de visualisation pour une analyse plus approfondie [#366](https://github.com/MTES-MCT/vizeau/pull/366).
- Ajout d'un affichage des analyses d'eau sous forme de tableau [#346](https://github.com/MTES-MCT/vizeau/pull/346).
- Ajout d'un champ "évolution cultures" pour suivre les changements dans le temps [#334](https://github.com/MTES-MCT/vizeau/pull/334).
- Amélioration de l'affichage des AACs avec un onglet dédié sur la page de visualisation [#333](https://github.com/MTES-MCT/vizeau/pull/333).
- Ajout d'un résumé des AACs sur la page de visualisation [#330](https://github.com/MTES-MCT/vizeau/pull/330).
- Ajout d'une indication de RPG (Rendement Potentiel en Graine) [#357](https://github.com/MTES-MCT/vizeau/pull/357).
- Possibilité de filtrer les AACs sur la page de visualisation [#364](https://github.com/MTES-MCT/vizeau/pull/364).
- Ajout de mini-cartes pour une meilleure navigation [#350](https://github.com/MTES-MCT/vizeau/pull/350).
- Implémentation d'une commande CLI pour assigner facilement des territoires aux utilisateurs [#376](https://github.com/MTES-MCT/vizeau/pull/376).
- Implémentation des permissions par territoire [#358](https://github.com/MTES-MCT/vizeau/pull/358).

### Évolutions techniques
- Mise en place d'un middleware Bouncer pour la gestion des autorisations et des politiques d'accès [#344](https://github.com/MTES-MCT/vizeau/pull/344).
- Correction d'un problème de suppression en cascade des entrées de journal [#322](https://github.com/MTES-MCT/vizeau/pull/322).
- Ajout d'une étape de build en pré-push pour garantir la qualité du code [#331](https://github.com/MTES-MCT/vizeau/pull/331).
- Amélioration de la gestion des dépendances et refactoring de composants UI [#355](https://github.com/MTES-MCT/vizeau/pull/355), [#338](https://github.com/MTES-MCT/vizeau/pull/338), [#337](https://github.com/MTES-MCT/vizeau/pull/337).

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur (gestion des formulaires de contact, affichage des données, etc.).
- Correction du texte affiché dans la popup des parcelles [#372](https://github.com/MTES-MCT/vizeau/pull/372).
- Correction du délai de debounce sur la recherche par raison sociale [#339](https://github.com/MTES-MCT/vizeau/pull/339).
- Correction d'un crash lors de la visualisation de données de culture manquantes [#347](https://github.com/MTES-MCT/vizeau/pull/347).
- Correction de la suppression du dernier contact supplémentaire [#363](https://github.com/MTES-MCT/vizeau/pull/363).
- Amélioration de la gestion inter-formulaires [#363](https://github.com/MTES-MCT/vizeau/pull/363).
- Correction de l'ID de l'icône pour le message de priorité dans le composant AacCaptages [#341](https://github.com/MTES-MCT/vizeau/pull/341).
