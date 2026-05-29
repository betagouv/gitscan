## Changelog : zero-logement-vacant (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la performance, la refactorisation du code pour une meilleure maintenabilité, et l'intégration des données LOVAC 2026. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, notamment au niveau de la gestion des campagnes et de la cartographie.

### Évolutions fonctionnelles
- Amélioration de l'UX de la légende de la carte : la légende est maintenant plus accessible et visuellement cohérente.  [#1825](https://github.com/MTES-MCT/zero-logement-vacant/issues/1825)
- Ajout d'une colonne "Statut de suivi" aux destinataires de campagne pour un meilleur suivi. [#1820](https://github.com/MTES-MCT/zero-logement-vacant/issues/1820)
- Redirection vers la vue tableau lors du clic sur le bouton de regroupement sur la carte. [#1823](https://github.com/MTES-MCT/zero-logement-vacant/issues/1823)
- Possibilité de trier les destinataires de campagne. [#1762](https://github.com/MTES-MCT/zero-logement-vacant/issues/1762)
- Suppression de l'ancien flux de campagne, simplifiant ainsi l'application. [#1783](https://github.com/MTES-MCT/zero-logement-vacant/issues/1783)
- Amélioration de l'exportation des groupes, avec l'ajout de la ville propriétaire et la différenciation de l'exportation de campagne. [#1761](https://github.com/MTES-MCT/zero-logement-vacant/issues/1761)

### Évolutions techniques
- Refactorisation importante du code, notamment suppression du préfixe `/api` sur les routes, suppression de code mort et amélioration de la structure des tests. [#1806](https://github.com/MTES-MCT/zero-logement-vacant/issues/1806), [#1790](https://github.com/MTES-MCT/zero-logement-vacant/issues/1790)
- Optimisation des performances de la requête de comptage des logements. [#1788](https://github.com/MTES-MCT/zero-logement-vacant/issues/1788)
- Amélioration de la gestion des statuts de logement, notamment pour les logements "jamais contactés". [#1804](https://github.com/MTES-MCT/zero-logement-vacant/issues/1804)
- Mise à jour des dépendances.
- Amélioration de la gestion des adresses BAN avec la synchronisation quotidienne et l'utilisation de Claude pour les changements dans l'entrepôt de données.
- Correction de problèmes liés à l'import des données LOVAC 2026. [#1812](https://github.com/MTES-MCT/zero-logement-vacant/issues/1812), [#1814](https://github.com/MTES-MCT/zero-logement-vacant/issues/1814), [#1815](https://github.com/MTES-MCT/zero-logement-vacant/issues/1815), [#1816](https://github.com/MTES-MCT/zero-logement-vacant/issues/1817)

### Autres changements
- Documentation améliorée concernant la suppression du préfixe `/api`.
- Ajout de compétences et documentation pour l'utilisation de Claude.
- Amélioration de la configuration des tests et correction de problèmes liés à la compilation des tests Dagster.
- Correction de problèmes de typographie dans l'interface utilisateur.
- Suppression de colonnes d'événements obsolètes.
- Mise à jour de la configuration de Nx.
