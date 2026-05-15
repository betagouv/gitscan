## Changelog : zero-logement-vacant (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration des performances, la refactorisation du code pour une meilleure maintenabilité, et l'enrichissement de la documentation technique. Des améliorations significatives ont également été apportées à la gestion des campagnes et à l'intégration des données, notamment avec le système BAN. L'interface utilisateur a été améliorée avec l'ajout d'une légende de carte plus conviviale.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur de la légende de la carte, avec un affichage plus clair et une meilleure ergonomie. [#1698](https://github.com/MTES-MCT/zero-logement-vacant/issues/1698)
- Possibilité de naviguer vers la liste des logements filtrée par campagne. [#1761](https://github.com/MTES-MCT/zero-logement-vacant/issues/1761)
- Différenciation de l'export de données pour les groupes et les campagnes, avec ajout de la colonne "ville propriétaire" pour l'export de groupe. [#1761](https://github.com/MTES-MCT/zero-logement-vacant/issues/1761)
- Correction du traitement des statuts de logement "jamais contacté". [#1794](https://github.com/MTES-MCT/zero-logement-vacant/issues/1794)
- Amélioration de l'alignement des boutons d'action des campagnes. [#1798](https://github.com/MTES-MCT/zero-logement-vacant/issues/1798)

### Évolutions techniques
- Suppression du préfixe `/api` des appels API en frontend et backend, simplifiant ainsi la configuration et améliorant la lisibilité du code. [#1806](https://github.com/MTES-MCT/zero-logement-vacant/issues/1806)
- Refactorisation du code lié aux campagnes, incluant la suppression de routes inutilisées et la simplification des gestionnaires. [#1810](https://github.com/MTES-MCT/zero-logement-vacant/issues/1810)
- Mise à jour des dépendances, incluant le remplacement de `vite-plugin-dts` par `unplugin-dts`. [#1805](https://github.com/MTES-MCT/zero-logement-vacant/issues/1805)
- Amélioration des performances du calcul du nombre de logements, réduisant le temps d'exécution de 4 à 36% selon les filtres. [#1793](https://github.com/MTES-MCT/zero-logement-vacant/issues/1793)
- Optimisation de la gestion des propriétaires multiples, avec l'ajout d'un indicateur `is_multi_owner` précalculé.
- Suppression du code obsolète lié à l'ancien flux de campagne.
- Migration de la documentation OpenAPI vers un format YAML et remplacement de Swagger UI par Scalar.
- Amélioration de la gestion des erreurs lors des appels à l'API BAN.
- Refactorisation de la configuration du serveur avec l'utilisation de Zod pour la validation.
- Amélioration des performances des requêtes de base de données liées aux propriétaires.
- Suppression de la synchronisation quotidienne du BAN.

### Autres changements
- Ajout de documentation technique complète, incluant des diagrammes et des explications détaillées des différents composants.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Mise à jour des compétences et des outils utilisés par l'équipe de développement.
- Amélioration de la configuration du CI/CD pour une meilleure automatisation du processus de déploiement.
- Ajout de métriques et d'alertes pour surveiller la santé de l'application.
- Ajout de la gestion des propriétaires avec un identifiant UUID.
- Ajout de la gestion des propriétaires CEREMA FF2025.
- Ajout de la documentation sur l'importation des DPE.
- Ajout de documentation sur la gestion des données.
- Ajout de documentation sur les processus de DE et DI.
- Ajout de documentation sur la génération automatique de la documentation.
- Ajout de documentation sur l'architecture de l'application.
