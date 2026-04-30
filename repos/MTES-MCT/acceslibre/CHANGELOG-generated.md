## Changelog : acceslibre (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités, notamment concernant la génération de rapports sur les ERP et l'intégration de l'API widget. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Possibilité de demander l'API widget par `asp_id` [#2580](https://github.com/MTES-MCT/acceslibre/issues/2580).
- Amélioration de l'affichage des détails des ERP avec une implémentation PDF, contrôlée par un *feature flag* [#2546](https://github.com/MTES-MCT/acceslibre/issues/2546) et [#2575](https://github.com/MTES-MCT/acceslibre/issues/2575).
- Correction d'un bug empêchant l'édition du type d'utilisateur si l'utilisateur n'est pas le propriétaire de l'ERP [#2576](https://github.com/MTES-MCT/acceslibre/issues/2576).
- Correction d'un bug lié à la question "pente" [#2600](https://github.com/MTES-MCT/acceslibre/issues/2600).
- Correction d'un bug lié aux détails de l'ERP [#2599](https://github.com/MTES-MCT/acceslibre/issues/2599).
- Amélioration de la recherche avec correction d'une erreur Sentry et support des combobox RGAAA [#2609](https://github.com/MTES-MCT/acceslibre/issues/2609).
- Correction d'une erreur Sentry lors de la génération de l'URL RPA [#2583](https://github.com/MTES-MCT/acceslibre/issues/2583).
- Utilisation de tuiles IGN avec repli sur Carto si hors métropole française [#2566](https://github.com/MTES-MCT/acceslibre/issues/2566).
- Export du code du widget [#2565](https://github.com/MTES-MCT/acceslibre/issues/2565).

### Évolutions techniques
- Utilisation d'un *feature flag* Django-waffle pour l'activation de la fonctionnalité RPA [#2578](https://github.com/MTES-MCT/acceslibre/issues/2578).
- Optimisation de la gestion des connexions à la base de données pour éviter les fuites [#2579](https://github.com/MTES-MCT/acceslibre/issues/2579).
- Amélioration des performances de statistiques [#2610](https://github.com/MTES-MCT/acceslibre/issues/2610).

### Autres changements
- Mise à jour de diverses dépendances (Sentry, Django, Redis, Celery, Faker, etc.). Ces mises à jour sont principalement des corrections de bugs et des améliorations de sécurité.
- Mise à jour des outils de développement (ESLint, Ruff, Prettier, Django Debug Toolbar).
