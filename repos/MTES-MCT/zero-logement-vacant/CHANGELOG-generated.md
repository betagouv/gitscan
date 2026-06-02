## Changelog : zero-logement-vacant (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances, la refactorisation du code pour une meilleure maintenabilité et la correction de bugs. Des améliorations significatives ont été apportées à la gestion des campagnes, notamment la suppression de l'ancien flux de campagne et l'ajout de nouvelles fonctionnalités pour l'exportation de données. L'application a également bénéficié d'une mise à jour de ses dépendances et d'optimisations pour l'importation des données LOVAC.

### Évolutions fonctionnelles
- Ajout d'une colonne "Statut de réception" aux destinataires de campagne, permettant de suivre l'état de la communication. [#1820](https://github.com/MTES-MCT/zero-logement-vacant/issues/1820)
- Amélioration de l'UX et du style visuel de la légende de la carte, avec un bouton pour l'afficher/masquer. [#1791](https://github.com/MTES-MCT/zero-logement-vacant/issues/1791)
- Possibilité de cliquer sur les noms de campagne dans les détails du logement pour accéder directement à la page de la campagne. [#1830](https://github.com/MTES-MCT/zero-logement-vacant/issues/1830)
- Redirection vers la vue tableau lors du clic sur le bouton de regroupement sur la carte. [#1829](https://github.com/MTES-MCT/zero-logement-vacant/issues/1829)
- Amélioration de l'alignement des boutons d'action des campagnes. [#1762](https://github.com/MTES-MCT/zero-logement-vacant/issues/1762)
- Ajout d'une différenciation pour l'exportation des groupes et des campagnes. [#1783](https://github.com/MTES-MCT/zero-logement-vacant/issues/1783)
- Ajout d'un état de chargement au bouton de connexion. [#1829](https://github.com/MTES-MCT/zero-logement-vacant/issues/1829)

### Évolutions techniques
- Mise à jour de React Router vers la version 7. [#1733](https://github.com/MTES-MCT/zero-logement-vacant/issues/1733)
- Suppression du préfixe `/api` des routes et des appels API pour simplifier l'architecture. [#1806](https://github.com/MTES-MCT/zero-logement-vacant/issues/1806)
- Refactorisation de la gestion des campagnes, avec suppression de l'ancien flux et simplification du code. [#1783](https://github.com/MTES-MCT/zero-logement-vacant/issues/1783)
- Optimisation des performances de la requête de comptage des logements. [#1793](https://github.com/MTES-MCT/zero-logement-vacant/issues/1793)
- Amélioration de la performance de l'importation des données LOVAC en utilisant `COPY FROM STDIN` au lieu de `psql`. [#1832](https://github.com/MTES-MCT/zero-logement-vacant/issues/1832)
- Mise à jour des dépendances npm et yarn. [#1808](https://github.com/MTES-MCT/zero-logement-vacant/issues/1808)
- Suppression du code mort et des dépendances inutilisées. [#1806](https://github.com/MTES-MCT/zero-logement-vacant/issues/1806)
- Amélioration de la gestion des statuts de logement "jamais contacté". [#1804](https://github.com/MTES-MCT/zero-logement-vacant/issues/1804)

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles instructions d'installation et de configuration. [#1828](https://github.com/MTES-MCT/zero-logement-vacant/issues/1828)
- Ajout de règles de workflow pour l'étiquetage et l'assignation des pull requests.
- Ajout de tests pour améliorer la couverture du code.
- Ajout de compétences et amélioration de la documentation pour l'utilisation de Claude.
- Correction de problèmes de typographie dans les exports.
- Amélioration de la documentation pour les jobs Dagster.
- Ajout de skills et mise à jour de la documentation pour l'utilisation de Claude.
- Mise à jour de la configuration du projet nx.
- Ajout de la gestion des erreurs et des logs.
- Suppression de fichiers inutiles.
- Correction de problèmes de linting.
