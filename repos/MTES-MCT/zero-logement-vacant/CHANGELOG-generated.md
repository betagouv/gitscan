## Changelog : zero-logement-vacant (30 derniers jours, au 17 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à la gestion des logements vacants, notamment des corrections de bugs, des optimisations de l'interface utilisateur et de nouvelles fonctionnalités pour faciliter l'analyse des données et la gestion des utilisateurs. Un effort important a été réalisé pour améliorer l'accessibilité et la robustesse de l'application, avec l'ajout d'un outil de réparation et l'amélioration des tests.

### Évolutions fonctionnelles
- Amélioration de la gestion des périmètres sur la carte : possibilité de les masquer/afficher et de les rendre plus visibles. [#1884](https://github.com/MTES-MCT/zero-logement-vacant/issues/1884)
- Correction de l'affichage des informations sur les propriétaires, notamment pour les adresses avec un score de zéro. [#1881](https://github.com/MTES-MCT/zero-logement-vacant/issues/1881)
- Correction de l'affichage du filtre "Année de vacance 2023". [#1875](https://github.com/MTES-MCT/zero-logement-vacant/issues/1875)
- Correction de la couleur des icônes de filtre pour correspondre à la charte graphique. [#1876](https://github.com/MTES-MCT/zero-logement-vacant/issues/1876)
- Amélioration de la gestion des structures multi-établissements pour les utilisateurs. [#1879](https://github.com/MTES-MCT/zero-logement-vacant/issues/1879)
- Ajout de la possibilité de rendre le champ "Date de naissance" optionnel lors de l'édition des propriétaires. [#1861](https://github.com/MTES-MCT/zero-logement-vacant/issues/1861)
- Correction du filtre intercommunal pour les DDT (Directions Départementales des Territoires). [#1867](https://github.com/MTES-MCT/zero-logement-vacant/issues/1867)
- Amélioration du tableau de bord d'analyse. [#1868](https://github.com/MTES-MCT/zero-logement-vacant/issues/1868)
- Ajout d'un outil pour lister les utilisateurs CEREMA LOVAC non enregistrés. [#1846](https://github.com/MTES-MCT/zero-logement-vacant/issues/1846)

### Évolutions techniques
- Ajout d'un outil de réparation (repair harness) pour identifier et corriger les anomalies dans les données. Cet outil inclut une CLI et des tests.
- Refonte de la gestion des factories pour les tests, avec une approche plus générique et basée sur Faker.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour de l'infrastructure de déploiement pour utiliser Terraform.
- Correction de bugs et améliorations de la performance du serveur.
- Amélioration de la gestion des événements et du streaming des données.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Correction d'un problème de débordement de la tooltip dans la liste des logements. [#1892](https://github.com/MTES-MCT/zero-logement-vacant/issues/1892)
- Correction d'un bug lié à la réinitialisation du sous-statut des lots de logements. [#1891](https://github.com/MTES-MCT/zero-logement-vacant/issues/1891)

### Autres changements
- Amélioration de la documentation, notamment pour l'accessibilité RGAA (Référentiel Général d'Amélioration de l'Accessibilité). [#1893](https://github.com/MTES-MCT/zero-logement-vacant/issues/1893)
- Mise à jour des dépendances.
- Corrections de style et de formatage du code.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Amélioration de la configuration et des scripts de déploiement.
- Ajout de seeds pour l'environnement de démonstration.
- Correction de la configuration de l'API pour le déploiement.
