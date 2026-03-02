## Changelog : admin_api_entreprise (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API Entreprise et de son interface d'administration se concentrent sur l'ajout de nouvelles fonctionnalités pour faciliter l'administration des API, l'amélioration de la sécurité et la correction de bugs. Des améliorations ont été apportées à la gestion des requêtes API, à l'intégration de nouvelles sources de données (CNOUS, DGFIP, URSSAF/MSA) et à la documentation. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un espace dédié aux requêtes API pour les équipes BizDevSupport [#2095](https://github.com/etalab/admin_api_entreprise/pull/2095).
- Affichage des tokens valides dans l'interface d'administration [#2031](https://github.com/etalab/admin_api_entreprise/pull/2031).
- Intégration de la nouvelle version v4 de l'API CNOUS étudiant boursier, incluant la gestion des radiations [#2029](https://github.com/etalab/admin_api_entreprise/pull/2129).
- Ajout d'une fiche pour l'API CNOUS étudiant boursier v4 avec les champs de radiation [#2132](https://github.com/etalab/admin_api_entreprise/pull/2132).
- Correction du mois renvoyé par l'API QF v2 (correction de M en M-1) [#2114](https://github.com/etalab/admin_api_entreprise/pull/2114).
- Ajout de données utiles pour l'API [#2122](https://github.com/etalab/admin_api_entreprise/pull/2122).
- Ajout de la documentation pour l'intégration des données FD URSSAF/MSA dans l'API effectifs [#2113](https://github.com/etalab/admin_api_entreprise/pull/2113).
- Ajout d'un lien vers un dashboard Metabase pour visualiser les requêtes API [#2130](https://github.com/etalab/admin_api_entreprise/pull/2130).
- Intégration de l'API CNAV/PSU en version beta [#2127](https://github.com/etalab/admin_api_entreprise/pull/2127).

### Évolutions techniques
- Refactorisation de la gestion des requêtes API en utilisant un pattern facade [#2120](https://github.com/etalab/admin_api_entreprise/pull/2120).
- Ajout de modèles `AuthorizationRequestSecuritySettings` pour une gestion plus fine du rate limiting et des listes blanches d'IP.
- Suppression des endpoints dépréciés du catalogue de l'API Particulier [#2079](https://github.com/etalab/admin_api_entreprise/pull/2079).
- Amélioration de la sécurité en renforçant les contrôles d'accès [#2115](https://github.com/etalab/admin_api_entreprise/pull/2115).

### Autres changements
- Mise à jour de la documentation pour préciser la plage d'années acceptées pour l'endpoint DGFIP (2006 à N-1) [#2138](https://github.com/etalab/admin_api_entreprise/pull/2138).
- Ajout du skill Claude Code pour automatiser les mises à jour de version [#2135](https://github.com/etalab/admin_api_entreprise/pull/2135).
- Mise à jour des fichiers OpenAPI locaux avec les dernières définitions [#2133](https://github.com/etalab/admin_api_entreprise/pull/2133).
- Ajout d'une adresse email administrateur dans le README [#2125](https://github.com/etalab/admin_api_entreprise/pull/2125).
- Mises à jour de plusieurs dépendances (Rack, Faraday, Rubocop, Brakeman, RSpec-rails, Nokogiri, binding_of_caller) pour assurer la stabilité et la sécurité de l'application.
