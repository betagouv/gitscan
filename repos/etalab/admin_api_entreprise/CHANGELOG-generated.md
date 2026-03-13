## Changelog : admin_api_entreprise (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API d'administration se concentrent sur l'amélioration de la gestion des accès et des tokens, l'ajout de nouvelles API (CNOUS, DGFIP, MSA), et l'amélioration de la documentation et du suivi des performances. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la gestion des délégations d'éditeurs [#2147](https://github.com/etalab/admin_api_entreprise/pull/2147).
- Possibilité pour les administrateurs de créer un nouveau token pour une demande d'autorisation validée [#2145](https://github.com/etalab/admin_api_entreprise/pull/2145).
- Affichage des tokens valides dans l'interface d'administration [#2031](https://github.com/etalab/admin_api_entreprise/pull/2031).
- Ajout de la nouvelle API CNOUS étudiant boursier v4 avec champs de radiation [#2129](https://github.com/etalab/admin_api_entreprise/pull/2129).
- Intégration de l'API DGFIP avec documentation sur la plage d'années acceptées (2006 à N-1) [#2138](https://github.com/etalab/admin_api_entreprise/pull/2138).
- Ajout de l'API MSA alerte date ressource [#2126](https://github.com/etalab/admin_api_entreprise/pull/2126).
- Ajout de l'API CNAV PSU en version bêta [#2127](https://github.com/etalab/admin_api_entreprise/pull/2127).
- Amélioration de l'affichage de l'historique des versions pour les endpoints GIP MDS effectifs [#2154](https://github.com/etalab/admin_api_entreprise/pull/2154).
- Ajout d'un lien vers un tableau de bord Metabase pour suivre les requêtes API dans l'interface d'administration [#2132](https://github.com/etalab/admin_api_entreprise/pull/2132).
- Mise à jour de la documentation des API EAJE et QF [#2122](https://github.com/etalab/admin_api_entreprise/pull/2122).

### Évolutions techniques
- Rotation annuelle du token webhook pour renforcer la sécurité [#2155](https://github.com/etalab/admin_api_entreprise/pull/2155).
- Refactorisation pour migrer les scopes des tokens vers les demandes d'autorisation [#2146](https://github.com/etalab/admin_api_entreprise/pull/2146).
- Amélioration de la gestion des erreurs Sentry en ignorant les erreurs ActionView::MissingTemplate [#2144](https://github.com/etalab/admin_api_entreprise/pull/2144).
- Utilisation de Turbo Frames pour charger l'état de ping des endpoints de manière asynchrone [#2151](https://github.com/etalab/admin_api_entreprise/pull/2151).
- Suppression des endpoints obsolètes du catalogue d'API [#2130](https://github.com/etalab/admin_api_entreprise/pull/2130).
- Mise à jour des fichiers OpenAPI locaux avec les dernières définitions [#2133](https://github.com/etalab/admin_api_entreprise/pull/2133).
- Correction d'un warning dans les spécifications RSpec [#2097](https://github.com/etalab/admin_api_entreprise/pull/2097).

### Autres changements
- Correction d'un lien ancré dans la barre latérale pour "Historique de version" [#2153](https://github.com/etalab/admin_api_entreprise/pull/2153).
- Mise à jour des dépendances (Rubocop, RSpec, Nokogiri, Rack, Faker) [#2150](https://github.com/etalab/admin_api_entreprise/pull/2150), [#2149](https://github.com/etalab/admin_api_entreprise/pull/2149), [#2148](https://github.com/etalab/admin_api_entreprise/pull/2143), [#2142](https://github.com/etalab/admin_api_entreprise/pull/2142), [#2141](https://github.com/etalab/admin_api_entreprise/pull/2141), [#2137](https://github.com/etalab/admin_api_entreprise/pull/2137), [#2136](https://github.com/etalab/admin_api_entreprise/pull/2135), [#2134](https://github.com/etalab/admin_api_entreprise/pull/2132), [#2128](https://github.com/etalab/admin_api_entreprise/pull/2125), [#2124](https://github.com/etalab/admin_api_entreprise/pull/2123).
- Rubocop : augmentation de la longueur maximale des classes à 150 [#2145](https://github.com/etalab/admin_api_entreprise/pull/2145).
- Ajout du skill Claude Code bump-version [#2135](https://github.com/etalab/admin_api_entreprise/pull/2135).
- Suppression d'une tâche inutile [#2133](https://github.com/etalab/admin_api_entreprise/pull/2133).
