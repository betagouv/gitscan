## Changelog : zero-logement-vacant (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de performance, notamment grâce à la mise en cache des données Metabase et à l'optimisation des requêtes. L'importation des données LOVAC 2026 a été améliorée avec une nouvelle architecture basée sur DuckDB et un pipeline Dagster. L'interface utilisateur a également été modernisée avec l'intégration de composants DSFR et l'implémentation de nouvelles fonctionnalités comme l'affichage des statuts des destinataires de campagne.

### Évolutions fonctionnelles
- Ajout d'une colonne "Statut" pour les destinataires de campagne, permettant de suivre leur progression. [#1820](https://github.com/MTES-MCT/zero-logement-vacant/issues/1820)
- Amélioration du lien entre les campagnes et les logements : un clic sur un groupe dans la carte redirige désormais vers la vue tableau correspondante. [#1821](https://github.com/MTES-MCT/zero-logement-vacant/issues/1821)
- Correction d'un bug où le filtre de campagne était appliqué de manière incorrecte lors de la navigation vers la liste des logements. [#1822](https://github.com/MTES-MCT/zero-logement-vacant/issues/1822)
- Correction de l'affichage du bouton de légende de la carte, qui utilisait un style DSFR incorrect. [#1825](https://github.com/MTES-MCT/zero-logement-vacant/issues/1825)
- Correction d'un bug qui empêchait la réinitialisation correcte des logements lors de la suppression d'une campagne. [#1826](https://github.com/MTES-MCT/zero-logement-vacant/issues/1826)
- Ajout d'un état de chargement au bouton de connexion. [#1795](https://github.com/MTES-MCT/zero-logement-vacant/issues/1795)
- Possibilité de filtrer les logements par année de vacance avec une option "inconsistency2023".
- Mise à jour de la configuration Terraform. [#1848](https://github.com/MTES-MCT/zero-logement-vacant/issues/1848)

### Évolutions techniques
- Migration vers React Router v7 pour une meilleure performance et une meilleure expérience utilisateur. [#1733](https://github.com/MTES-MCT/zero-logement-vacant/issues/1733)
- Refactorisation importante du code frontend pour réduire la taille du bundle JavaScript de 73% grâce à la séparation des routes avec React.lazy. [#1833](https://github.com/MTES-MCT/zero-logement-vacant/issues/1833)
- Implémentation d'un cache pour les données Metabase afin d'améliorer les performances de la page d'analyse. [#1847](https://github.com/MTES-MCT/zero-logement-vacant/issues/1847)
- Nouvelle architecture pour l'importation des données LOVAC 2026, basée sur DuckDB et un pipeline Dagster pour une meilleure performance et fiabilité.
- Utilisation de Parquet pour le stockage des données LOVAC.
- Migration des tests vers Jest et Cypress.
- Suppression de l'utilisation de express-validator et remplacement par validatorNext pour une meilleure gestion de la validation.
- Suppression de l'ancien code DSFR et migration vers les composants DSFR natifs.
- Mise à jour des dépendances npm et yarn. [#1823](https://github.com/MTES-MCT/zero-logement-vacant/issues/1823)
- Remplacement de lodash/fp par effect.
- Utilisation de UUID v5 pour la génération d'identifiants uniques.

### Autres changements
- Amélioration de la documentation et ajout de plans d'implémentation pour les nouvelles fonctionnalités.
- Correction de problèmes de linting et de formatage du code.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des instructions de configuration.
- Ajout de compétences et finalisation de la construction de LOVAC avec de nombreux retours.
- Ajout de règles de workflow PR pour l'étiquetage et l'attribution des pull requests.
- Suppression de fichiers inutiles et nettoyage du code.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Correction de problèmes de typographie (utilisation des apostrophes françaises).
- Mise à jour des fichiers `.env.example` et des instructions d'onboarding.
- Ajout d'un outil de suivi des refactorings.
