## Changelog : plusfraichemaville-site (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration du module d'aides financières, notamment en termes d'expérience utilisateur et de gestion des données. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance du site. La gestion des collectivités et l'intégration avec l'API adresse ont également été améliorées.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur pour le choix des aides : UX amélioré pour la sélection des aides [#467](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/467).
- Ajout d'un badge "Déjà vu" sur les cartes d'aide pour indiquer les aides déjà sélectionnées [#468](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/468).
- Amélioration du lecteur mode pour une meilleure expérience de consultation [#473](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/473).
- Affichage du nombre d'aides sélectionnées dans le filtre.
- Possibilité de voir les projets associés à une collectivité (EPCI ou commune) [#469](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/469).
- Gestion des collectivités : ajout d'alertes Mattermost si un utilisateur n'a pas de SIREN [#465](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/465).
- Modification de la logique d'affichage des projets disponibles.
- Changement d'API adresse pour une meilleure fiabilité [#464](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/464).
- Amélioration de l'ouverture du modal de création d'estimation [#474](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/474).
- Ajout de la possibilité d'ajouter et supprimer des fiches solutions à une estimation.
- Affichage d'un avertissement de prix pour les territoires ultramarins [#470](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/470).

### Évolutions techniques
- Suppression du code lié à HubSpot et au lien vers les fonds verts [#471](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/471), [#472](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/472).
- Mise à jour de Next.js et jspdf [#466](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/466).
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Correction de la gestion des erreurs lors de la récupération des données LCZ.
- Suppression du champ `fiches_solutions_id` dans la table `estimations`.
- Migration de la table `estimations_aides` vers `projet_aide`.
- Ajout de scripts pour peupler les nouvelles tables EPCI et commune.
- Correction de plusieurs bugs et améliorations de la stabilité.

### Autres changements
- Nettoyage du code à plusieurs endroits.
- Amélioration de la gestion des breadcrumbs.
- Correction de problèmes de linting et de formatage du code.
- Suppression de liens inutiles.
- Ajustement des marges pour correspondre au design.
