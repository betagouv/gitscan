## Changelog : zero-logement-vacant (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de performance, notamment grâce à la mise en cache de données Metabase et à l'optimisation des requêtes. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'importation de données LOVAC 2026 et l'affichage des données sur la carte, ainsi que des corrections de bugs et des améliorations de l'expérience utilisateur. L'architecture a également été modernisée avec la migration vers React Router v7 et l'adoption de nouvelles bibliothèques comme `@gouvfr/dsfr-chart`.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les logements par campagne. [#1822](https://github.com/MTES-MCT/zero-logement-vacant/issues/1822)
- Ajout d'une colonne "Statut" dans le tableau des bénéficiaires de campagne pour suivre l'état de la prise en charge. [#1820](https://github.com/MTES-MCT/zero-logement-vacant/issues/1820)
- Amélioration de la navigation : un clic sur un groupe sur la carte redirige maintenant vers le tableau correspondant. [#1821](https://github.com/MTES-MCT/zero-logement-vacant/issues/1821)
- Mise en place d'un système de cache pour les données Metabase afin d'améliorer les performances de la page d'analyse. [#1847](https://github.com/MTES-MCT/zero-logement-vacant/issues/1847)
- Implémentation d'un cache pour les données de la page d'analyse, conservant les données pendant 1 heure.
- Ajout d'une nouvelle fonctionnalité permettant d'importer les données LOVAC 2026. [#1773](https://github.com/MTES-MCT/zero-logement-vacant/issues/1773)
- Ajout d'une option pour spécifier l'année de vacance (avec une option "inconsistency2023").
- Amélioration de l'affichage des logements sur la carte avec des boutons DSFR correctement stylisés. [#1825](https://github.com/MTES-MCT/zero-logement-vacant/issues/1825)
- Ajout d'un état de chargement au bouton de connexion. [#1795](https://github.com/MTES-MCT/zero-logement-vacant/issues/1795)

### Évolutions techniques
- Migration vers React Router v7. [#1733](https://github.com/MTES-MCT/zero-logement-vacant/issues/1733)
- Refactorisation importante du code pour supprimer l'utilisation de la bibliothèque DSFR obsolète. [#1850](https://github.com/MTES-MCT/zero-logement-vacant/issues/1850)
- Adoption de la bibliothèque `@gouvfr/dsfr-chart` pour l'affichage de graphiques DSFR natifs. [#1844](https://github.com/MTES-MCT/zero-logement-vacant/issues/1844)
- Utilisation de DuckDB pour le prétraitement des données LOVAC et la correction des codes géographiques.
- Optimisation des requêtes SQL pour l'importation des données LOVAC.
- Amélioration de la gestion des erreurs et des tests.
- Refactorisation de la gestion des filtres de logement en utilisant un React Context Provider. [#1848](https://github.com/MTES-MCT/zero-logement-vacant/issues/1848)
- Utilisation de `tsx` au lieu de `ts-node`.
- Mise à jour des dépendances npm et yarn. [#1823](https://github.com/MTES-MCT/zero-logement-vacant/issues/1823)
- Amélioration de la structure du projet avec l'utilisation de `nx`.
- Migration vers une nouvelle approche de validation avec `zod`.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture.
- Ajout de plans d'implémentation et de spécifications de conception pour les nouvelles fonctionnalités.
- Amélioration de la configuration et des scripts de déploiement.
- Correction de problèmes de linting et de formatage du code.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Ajout d'un script pour mettre à jour la configuration Terraform. [#1849](https://github.com/MTES-MCT/zero-logement-vacant/issues/1849)
- Mise à jour des compétences de l'équipe.
- Ajout d'un workflow pour partager les plugins Claude avec l'équipe. [#1859](https://github.com/MTES-MCT/zero-logement-vacant/issues/1859)
