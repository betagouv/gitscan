## Changelog : admin_api_entreprise (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API d'administration se concentrent sur l'amélioration de la gestion des API Entreprise et Particulier, avec des ajouts de fonctionnalités pour le support BizDev, l'ajout de nouvelles API (CNOUS étudiant boursier v4, CNAV/PSU), et des corrections de bugs pour assurer une meilleure précision des données et une expérience utilisateur plus fluide. Des efforts ont également été faits pour renforcer la sécurité et la documentation.

### Évolutions fonctionnelles
- Ajout d'un espace dédié aux requêtes API pour l'équipe BizDev Support [#2095](https://github.com/etalab/admin_api_entreprise/pull/2095).
- Intégration de la nouvelle API CNOUS étudiant boursier v4, incluant les champs de radiation [#2129](https://github.com/etalab/admin_api_entreprise/pull/2129).
- Ajout de la nouvelle API CNAV/PSU en version bêta [#2127](https://github.com/etalab/admin_api_entreprise/pull/2127).
- Correction du mois renvoyé par l'API QF v2, qui affichait "M" au lieu de "M-1" [#2114](https://github.com/etalab/admin_api_entreprise/pull/2114).
- Amélioration de l'affichage des données utiles [#2122](https://github.com/etalab/admin_api_entreprise/pull/2122).
- Documentation mise à jour pour les API EAJE et QF [#2122](https://github.com/etalab/admin_api_entreprise/pull/2122).
- Ajout d'un lien vers un tableau de bord Metabase pour les requêtes API dans l'interface d'administration [#2132](https://github.com/etalab/admin_api_entreprise/pull/2132).
- Affichage des tokens valides [#2031](https://github.com/etalab/admin_api_entreprise/pull/2031).

### Évolutions techniques
- Migration des scopes des tokens vers les requêtes d'autorisation [#2146](https://github.com/etalab/admin_api_entreprise/pull/2146).
- Intégration de Sentry pour le suivi des erreurs, avec une gestion spécifique des erreurs `ActionView::MissingTemplate` [#2144](https://github.com/etalab/admin_api_entreprise/pull/2144).
- Mise à jour de plusieurs dépendances : Faraday (2.14.0 -> 2.14.1), Rubocop (1.84.0 -> 1.84.1 -> 1.84.2 -> 1.85.0), Nokogiri (1.19.0 -> 1.19.1), Rack (3.2.4 -> 3.2.5), rspec-rails, binding_of_caller.
- Suppression d'une tâche inutile.
- Amélioration de la sécurité générale [#2115](https://github.com/etalab/admin_api_entreprise/pull/2115).
- Mise à jour des fichiers OpenAPI locaux [#2133](https://github.com/etalab/admin_api_entreprise/pull/2133).
- Suppression des endpoints dépréciés du catalogue API Particulier [#2130](https://github.com/etalab/admin_api_entreprise/pull/2130).

### Autres changements
- Ajout d'un nouveau skill Claude Code pour automatiser le bump de version [#2131](https://github.com/etalab/admin_api_entreprise/pull/2131).
- Documentation de la plage d'années acceptée (2006 à N-1) pour l'endpoint DGFIP [#2138](https://github.com/etalab/admin_api_entreprise/pull/2138).
- Correction de warnings dans les specs [#2097](https://github.com/etalab/admin_api_entreprise/pull/2097).
- Mise en forme des informations QF et de la composition familiale.
- Ajout d'une date pour les strings au format date.
