## Changelog : zero-logement-vacant (30 derniers jours, au 04 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration avec Metabase pour l'analyse de données, l'optimisation des performances (notamment au niveau de la base de données et du chargement initial de l'application), et l'ajout de nouvelles fonctionnalités comme l'affichage des statuts des destinataires de campagnes et l'amélioration de l'export de données. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une nouvelle vue "Analyse" utilisant des graphiques natifs de Metabase (DSFR) pour la visualisation des données. [#1834](https://github.com/MTES-MCT/zero-logement-vacant/issues/1834)
- Possibilité de lier les noms de campagne directement aux logements dans la vue de détail. [#1830](https://github.com/MTES-MCT/zero-logement-vacant/issues/1830)
- Ajout d'une colonne "Statut" dans le tableau des destinataires de campagne, affichant le statut de suivi. [#1820](https://github.com/MTES-MCT/zero-logement-vacant/issues/1820)
- Amélioration de l'UX de la légende de la carte, avec un bouton dédié et un style DSFR. [#1823](https://github.com/MTES-MCT/zero-logement-vacant/issues/1823)
- Possibilité de passer à la vue tableau depuis la carte en cliquant sur un groupe de logements. [#1832](https://github.com/MTES-MCT/zero-logement-vacant/issues/1832)
- Simplification de la création de campagnes en rendant la description optionnelle. [#1824](https://github.com/MTES-MCT/zero-logement-vacant/issues/1824)
- Ajout d'un état de chargement au bouton de connexion. [#1829](https://github.com/MTES-MCT/zero-logement-vacant/issues/1829)

### Évolutions techniques
- Mise à jour de React Router vers la version 7. [#1733](https://github.com/MTES-MCT/zero-logement-vacant/issues/1733)
- Refactorisation importante pour supprimer le préfixe `/api` des routes, simplifiant ainsi l'architecture. [#1806](https://github.com/MTES-MCT/zero-logement-vacant/issues/1806)
- Optimisation des performances du chargement initial de l'application en utilisant `React.lazy` pour diviser les bundles de routes. Réduction de 73% de la taille du JavaScript initial. [#1833](https://github.com/MTES-MCT/zero-logement-vacant/issues/1833)
- Amélioration des performances de la base de données en remplaçant un index géographique par un index combiné `(owner_id, rank)` sur la table `owners_housing`.
- Remplacement de la requête dynamique pour déterminer si un logement a plusieurs propriétaires par une colonne `is_multi_owner` précalculée.
- Utilisation de `pg COPY FROM STDIN` pour un chargement plus rapide des données en masse.
- Refactorisation du script d'importation des propriétaires pour exporter les données au format Parquet.
- Amélioration de la gestion des erreurs et de la résolution des dépendances pour le worker PDF.
- Mise à jour des dépendances et correction de problèmes liés à la configuration.

### Autres changements
- Documentation mise à jour pour refléter les changements de configuration et d'installation.
- Corrections de tests et amélioration de la couverture de tests.
- Ajout de règles de workflow pour l'étiquetage et l'attribution des pull requests.
- Amélioration de la gestion des typographies françaises (apostrophes).
- Ajout de la skill "mise-en-production" dans le fichier de configuration.
- Suppression de code inutile et amélioration de la lisibilité du code.
- Correction de problèmes de linting et de style.
- Ajout de documentation pour l'intégration avec Metabase.
- Suppression de l'export de la feuille des propriétaires dans l'export de groupe.
- Correction de problèmes liés à l'importation des données LOVAC 2026.
