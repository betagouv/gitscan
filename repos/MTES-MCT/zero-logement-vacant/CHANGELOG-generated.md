## Changelog : zero-logement-vacant (30 derniers jours, au 2026-05-19)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances et de la robustesse de la plateforme, notamment au niveau du pipeline de données (dbt) et de l'application elle-même. Des corrections ont été apportées pour améliorer la qualité des données et résoudre des problèmes liés à l'importation des données LOVAC 2026.  Des refactorings importants ont été réalisés pour simplifier le code, supprimer des fonctionnalités obsolètes et préparer l'application pour de futures améliorations.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur de la légende de la carte, avec une meilleure visibilité et un style plus clair [#1698](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1698).
- Possibilité de naviguer vers la liste des logements filtrée par campagne directement depuis l'interface.
- Amélioration de l'export des données de groupe, avec l'ajout de la colonne "ville propriétaire" et des ajustements de formatage.
- Correction du traitement du statut des logements "jamais contacté".
- Suppression de l'ancien flux de gestion des campagnes, simplifiant ainsi l'application et réduisant sa complexité.

### Évolutions techniques
- **dbt:** Optimisations significatives du pipeline de données pour améliorer les performances et la gestion de la mémoire, notamment lors de la phase de matching des propriétaires.
- **dbt:** Ajout de l'identifiant UUID des propriétaires pour améliorer la traçabilité et la cohérence des données.
- Suppression du préfixe `/api` des routes de l'API, simplifiant ainsi la configuration et l'utilisation de l'application.
- Refactorings importants du code frontend et backend pour supprimer du code obsolète, améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances, incluant des corrections de version et l'utilisation de nouveaux outils de build.
- Amélioration des tests, avec correction de tests existants et ajout de nouveaux tests pour garantir la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Suppression de code lié à des fonctionnalités abandonnées (anciens flux de campagne, établissement).

### Autres changements
- Documentation mise à jour pour refléter les changements apportés à l'application.
- Ajout de spécifications pour la suppression de l'ancien flux de campagne.
- Ajout de nouveaux agents et compétences Claude pour l'amélioration continue du data warehouse.
- Amélioration de la configuration et de l'environnement de développement.
- Corrections de linting et de style de code.
