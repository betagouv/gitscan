## Changelog : acceslibre (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la stabilité de la plateforme, notamment au niveau de la gestion des données RPA et de l'interface utilisateur. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, ainsi que l'introduction de fonctionnalités contrôlées par des *feature flags* pour faciliter les déploiements progressifs.

### Évolutions fonctionnelles
- Possibilité de demander l'API du widget par `asp_id` [#2580](https://github.com/MTES-MCT/acceslibre/issues/2580).
- Amélioration de la recherche "Où" avec correction d'une erreur Sentry et support des combobox RGAAA [#2609](https://github.com/MTES-MCT/acceslibre/issues/2609).
- Mise en place d'un mécanisme pour désindexer les PDF RPA [#2611](https://github.com/MTES-MCT/acceslibre/issues/2611).
- Implémentation de la génération de PDF pour les détails des ERP (contrôlée par *feature flag*) [#2546](https://github.com/MTES-MCT/acceslibre/issues/2546) et [#2575](https://github.com/MTES-MCT/acceslibre/issues/2575).
- Correction d'un bug lié à l'affichage des informations "à propos" [#2577](https://github.com/MTES-MCT/acceslibre/issues/2577).
- Restriction de la modification du type d'utilisateur aux propriétaires de l'ERP [#2576](https://github.com/MTES-MCT/acceslibre/issues/2576).

### Évolutions techniques
- Optimisations de performance générales, notamment au niveau des statistiques [#2610](https://github.com/MTES-MCT/acceslibre/issues/2610).
- Utilisation de *feature flags* (django-waffle) pour contrôler le déploiement de la fonctionnalité RPA [#2578](https://github.com/MTES-MCT/acceslibre/issues/2578).
- Amélioration de la gestion des connexions à la base de données pour éviter les problèmes de réouverture [#2579](https://github.com/MTES-MCT/acceslibre/issues/2579).
- Corrections de bugs et améliorations liées à l'URL de génération des RPA [#2582](https://github.com/MTES-MCT/acceslibre/issues/2582) et [#2583](https://github.com/MTES-MCT/acceslibre/issues/2583).
- Corrections de bugs liés à la logique de l'étape 2 [#2600](https://github.com/MTES-MCT/acceslibre/issues/2600) et [#2599](https://github.com/MTES-MCT/acceslibre/issues/2599).

### Autres changements
- Mise à jour de la documentation et de la configuration pour supporter les nouvelles fonctionnalités.
- Diverses mises à jour de dépendances (voir les commits dependabot).
